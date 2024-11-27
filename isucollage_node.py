import torch
import math

class IsuCollageNode:
    """
    Intelligent Image Collage Generator
    Preserving image characteristics, inspired by react-isucollage
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "target_row_height": ("INT", {"default": 300, "min": 100, "max": 1024, "step": 50}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("collage_image",)
    FUNCTION = "create_collage"
    CATEGORY = "Isulion/Image"

    def create_collage(self, images, target_row_height=300):
        """
        Create a collage that preserves image characteristics.
        
        :param images: List of image tensors
        :param target_row_height: Target height for image rows
        :return: Collage image tensor
        """
        # Handle edge cases
        if not images:
            raise ValueError("No images provided")
        if len(images) == 1:
            # Ensure the single image is in the correct format
            return images[0] if len(images[0].shape) == 3 else images[0][0]

        # Ensure all images are in the correct format (H, W, C)
        processed_images = []
        for img in images:
            # Convert 4D tensor to 3D if needed
            if len(img.shape) == 4:
                img = img.squeeze(0)
            processed_images.append(img)

        # Compute aspect ratios
        aspect_ratios = [
            img.shape[1] / img.shape[0]  # Width / Height 
            for img in processed_images
        ]
        
        # Distribute images across rows
        rows = self._distribute_images(processed_images, aspect_ratios)
        
        # Normalize and prepare rows
        normalized_rows = self._normalize_rows(rows, target_row_height)
        
        # Stack rows vertically
        collage_tensor = self._stack_rows(normalized_rows)
        
        # Ensure the output is a 4D tensor for ComfyUI
        return (collage_tensor[None, ...],)

    def _distribute_images(self, images, aspect_ratios):
        """
        Distribute images across rows to maximize canvas utilization.
        
        :param images: List of image tensors
        :param aspect_ratios: Corresponding aspect ratios
        :return: List of rows with distributed images
        """
        # Sort images by aspect ratio in descending order
        sorted_indices = sorted(
            range(len(aspect_ratios)), 
            key=lambda k: aspect_ratios[k], 
            reverse=True
        )
        
        # Compute optimal row configuration
        num_images = len(images)
        num_rows = max(1, math.ceil(math.sqrt(num_images)))
        
        # Initialize rows
        rows = [[] for _ in range(num_rows)]
        
        # Distribute images across rows
        for idx in sorted_indices:
            # Find row with least total width
            target_row = min(range(num_rows), key=lambda r: sum(
                img.shape[1] for img in rows[r]
            ))
            rows[target_row].append(images[idx])
        
        return rows

    def _normalize_rows(self, rows, target_height):
        """
        Normalize rows to completely fill the canvas with no empty spaces.
        
        :param rows: List of image rows
        :param target_height: Desired row height
        :return: Normalized rows of images
        """
        # Find the maximum total width across all rows
        max_total_width = max(
            sum(img.shape[1] for img in row) 
            for row in rows
        )
        
        normalized_rows = []
        for row in rows:
            # Skip empty rows
            if not row:
                continue
            
            # Compute consistent height for the row
            row_heights = [img.shape[0] for img in row]
            consistent_height = min(row_heights)
            
            # Resize images to consistent height and calculate total width
            resized_row = []
            for img in row:
                # Ensure tensor has 3 dimensions (H, W, C)
                if len(img.shape) == 4:
                    img = img.squeeze(0)
                
                # Calculate new width maintaining aspect ratio
                aspect_ratio = img.shape[1] / img.shape[0]
                new_width = int(consistent_height * aspect_ratio)
                
                # Resize image
                resized_img = self._resize_to_exact(
                    img, 
                    (consistent_height, new_width)
                )
                resized_row.append(resized_img)
            
            # Normalize row width precisely
            normalized_row = self._normalize_row_width(resized_row, max_total_width)
            normalized_rows.append(normalized_row)
        
        return normalized_rows

    def _normalize_row_width(self, row, target_width):
        """
        Normalize a single row to exactly match the target width.
        
        :param row: List of image tensors in a row
        :param target_width: Desired total width for the row
        :return: Normalized row with images precisely matching target width
        """
        # Current row width
        current_width = sum(img.shape[1] for img in row)
        
        # If current width matches target, return as-is
        if current_width == target_width:
            return row
        
        # Determine which images to adjust
        normalized_row = []
        remaining_adjustment = target_width - current_width
        
        # Sort images by width to ensure most predictable adjustment
        sorted_indices = sorted(
            range(len(row)), 
            key=lambda i: row[i].shape[1], 
            reverse=True
        )
        
        # Distribute adjustment across images
        for i, idx in enumerate(sorted_indices):
            img = row[idx]
            
            # Calculate proportional width adjustment
            img_width_ratio = img.shape[1] / current_width
            
            # Determine width adjustment
            if i == 0:
                # First (widest) image gets the full remaining adjustment
                width_adjustment = remaining_adjustment
            else:
                # Proportional adjustment for other images
                width_adjustment = 0
            
            # Resize image
            new_width = img.shape[1] + width_adjustment
            resized_img = self._resize_to_exact(
                img, 
                (img.shape[0], new_width)
            )
            
            # Replace or add to normalized row
            if i < len(normalized_row):
                normalized_row[idx] = resized_img
            else:
                normalized_row.append(resized_img)
        
        # Verify final width with tolerance
        final_width = sum(img.shape[1] for img in normalized_row)
        
        # Debug print
        print(f"\n--- WIDTH NORMALIZATION DEBUG ---")
        print(f"Target Width: {target_width}")
        print(f"Final Width: {final_width}")
        for i, img in enumerate(normalized_row):
            print(f"Image {i} width: {img.shape[1]}")
        
        # Allow minimal tolerance due to integer rounding
        assert abs(final_width - target_width) <= 1, \
            f"Width mismatch: {final_width} != {target_width}"
        
        return normalized_row

    def _stack_rows(self, rows):
        """
        Stack rows vertically to create the final collage.
        
        :param rows: List of rows, each row is a list of image tensors
        :return: Final collage tensor
        """
        # Debug: Print input row information
        print("\n--- ROW STACKING DEBUG ---")
        for i, row in enumerate(rows):
            print(f"Row {i} images:")
            for j, img in enumerate(row):
                print(f"  Image {j} shape: {img.shape}")
        
        # Concatenate rows horizontally first
        row_tensors = []
        for row in rows:
            # Concatenate images in the row
            row_tensor = torch.cat(row, dim=1)
            row_tensors.append(row_tensor)
        
        # Stack rows vertically
        try:
            collage_tensor = torch.cat(row_tensors, dim=0)
            
            # Debug: Final collage tensor
            print("\n--- FINAL COLLAGE DEBUG ---")
            print(f"Collage tensor shape: {collage_tensor.shape}")
            
            return collage_tensor
        except Exception as e:
            print(f"\n!!! STACKING ERROR: {e}")
            # Print detailed row information for debugging
            for i, row in enumerate(row_tensors):
                print(f"Row {i} details: {row.shape}")
            raise

    def _resize_to_exact(self, tensor, target_size):
        """
        Resize image tensor to exact size.
        
        :param tensor: Input image tensor
        :param target_size: (height, width) tuple
        :return: Resized tensor
        """
        # Efficient resizing with minimal memory overhead
        # Ensure tensor is 3D
        if len(tensor.shape) == 4:
            tensor = tensor.squeeze(0)
        
        # Add batch dimension for interpolate
        tensor_4d = tensor.unsqueeze(0).permute(0, 3, 1, 2)
        
        resized_tensor = torch.nn.functional.interpolate(
            tensor_4d,
            size=target_size,
            mode='nearest'  # Preserves image characteristics
        )
        
        # Convert back to original format
        return resized_tensor.permute(0, 2, 3, 1).squeeze(0)