from typing import Dict
from .base_handler import BaseThemeHandler

class FuturisticCityThemeHandler(BaseThemeHandler):
    """Handler for futuristic city-themed prompt generation."""
    
    def generate(self, custom_subject: str = "",
                custom_location: str = "",
                include_environment: str = "yes",
                include_style: str = "yes",
                include_effects: str = "yes") -> Dict[str, str]:
        """Generate futuristic city-themed components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            components["subject"] = (
                f"((ultra-modern {custom_subject})), "
                f"((futuristic design)), ((high-tech aesthetics)), "
                f"((advanced architecture))"
            )
        else:
            structure = self._get_random_choice("futuristic_city.structures")
            material = self._get_random_choice("futuristic_city.materials")
            feature = self._get_random_choice("futuristic_city.features")
            components["subject"] = (
                f"((ultra-modern {structure})) made of ((advanced {material})), "
                f"((featuring {feature})), ((futuristic design)), "
                f"((high-tech aesthetics)), ((advanced architecture))"
            )
        
        # Generate environment if requested
        if include_environment == "yes":
            if custom_location:
                components["environment"] = (
                    f"in ((futuristic {custom_location})) with "
                    f"((advanced technology)), ((sci-fi atmosphere))"
                )
            else:
                cityscape = self._get_random_choice("futuristic_city.cityscapes")
                tech = self._get_random_choice("futuristic_city.technology")
                components["environment"] = (
                    f"in ((advanced {cityscape})) with "
                    f"((integrated {tech})), "
                    f"((high-tech environment)), ((sci-fi atmosphere))"
                )
        
        # Generate style if requested
        if include_style == "yes":
            style = self._get_random_choice("futuristic_city.styles")
            aesthetic = self._get_random_choice("futuristic_city.aesthetics")
            components["style"] = (
                f"((rendered in {style} style)), "
                f"((with {aesthetic} aesthetic)), "
                f"((ultra-modern design)), ((technological advancement)), "
                f"((clean futuristic look))"
            )
        
        # Generate effects if requested
        if include_effects == "yes":
            lighting = self._get_random_choice("futuristic_city.lighting")
            atmosphere = self._get_random_choice("futuristic_city.atmosphere")
            components["effects"] = (
                f"with ((advanced {lighting} lighting)), "
                f"((futuristic {atmosphere})), "
                f"((high-tech ambiance)), ((sci-fi mood))"
            )
        
        return components
