import json
import random
import os

class VideoPromptGenerator:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                      "configs", "video_prompt_config.json")
        self.load_config()
    
    @classmethod
    def INPUT_TYPES(cls):
        try:
            config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                      "configs", "video_prompt_config.json")
            with open(config_path, 'r') as f:
                config = json.load(f)
                camera_angles = ["Random"] + config["camera_angles"]
                lighting_conditions = ["Random"] + config["lighting_conditions"]
        except Exception as e:
            print(f"Error loading config for INPUT_TYPES: {e}")
            camera_angles = ["Random", "The camera remains stationary"]
            lighting_conditions = ["Random", "with natural lighting"]

        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "custom_subject": ("STRING", {"default": "", "multiline": False}),
                "custom_location": ("STRING", {"default": "", "multiline": False}),
                "camera_angle": (camera_angles,),
                "lighting": (lighting_conditions,),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Isulion/Prompt"

    def load_config(self):
        try:
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = {
                "subjects": ["a person"],
                "locations": ["in a room"],
                "camera_angles": ["The camera remains stationary"],
                "lighting_conditions": ["with natural lighting"]
            }

    def generate_prompt(self, seed, custom_subject="", custom_location="", camera_angle="", lighting=""):
        # Set random seed for reproducibility
        rng = random.Random(seed)
        
        # Use custom values if provided, otherwise use random values
        subject = custom_subject if custom_subject else rng.choice(self.config["subjects"])
        
        # Handle location with proper preposition
        if custom_location:
            # Check if location already starts with a preposition
            prepositions = ["in", "at", "near", "by", "inside", "outside"]
            has_preposition = any(custom_location.lower().startswith(prep) for prep in prepositions)
            location = custom_location if has_preposition else f"in {custom_location}"
        else:
            location = rng.choice(self.config["locations"])
        
        # Handle camera angle and lighting with Random option
        camera = rng.choice(self.config["camera_angles"]) if camera_angle == "Random" else camera_angle
        lighting_condition = rng.choice(self.config["lighting_conditions"]) if lighting == "Random" else lighting

        # Construct a detailed, cinematographic prompt
        prompt = f"{subject} {location}. "
        prompt += f"{camera}, capturing the scene as {lighting_condition}. "
        prompt += "The scene unfolds naturally, with fluid movements and authentic expressions. "
        prompt += "The overall composition maintains a cinematic quality with attention to detail and depth."

        return (prompt,)

NODE_CLASS_MAPPINGS = {
    "Isulion Video Prompt Generator 🎥": VideoPromptGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Isulion Video Prompt Generator 🎥": "Isulion Video Prompt Generator 🎥"
}
