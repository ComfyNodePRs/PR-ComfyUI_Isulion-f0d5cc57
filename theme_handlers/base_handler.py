from abc import ABC, abstractmethod
from typing import Dict, Optional

class BaseThemeHandler(ABC):
    """Base class for all theme handlers."""
    
    def __init__(self, config_manager):
        """Initialize the theme handler with configuration manager."""
        self.config = config_manager
    
    @abstractmethod
    def generate(self, custom_subject: str = "", 
                custom_location: str = "",
                include_environment: str = "yes",
                include_style: str = "yes",
                include_effects: str = "yes") -> Dict[str, str]:
        """Generate theme-specific components.
        
        Args:
            custom_subject (str): Custom subject override
            custom_location (str): Custom location override
            include_environment (str): Whether to include environment
            include_style (str): Whether to include style
            include_effects (str): Whether to include effects
            
        Returns:
            Dict[str, str]: Dictionary containing generated components
        """
        pass
    
    def _get_random_choice(self, config_key: str) -> str:
        """Get a random choice from configuration list.
        
        Args:
            config_key (str): Key to access in configuration
            
        Returns:
            str: Random choice from the configuration list
        """
        choices = self.config.get_config(config_key)
        if not choices:
            # Default values for different types of configurations
            defaults = {
                "characters": "character",
                "outfits": "outfit",
                "poses": "pose",
                "expressions": "expression",
                "emotions": "emotion",
                "locations": "location",
                "styles": "style",
                "effects": "effect",
                "textures": "texture",
                "patterns": "pattern",
                "shapes": "shape",
                "motions": "motion",
                "color_schemes": "color scheme",
                "techniques": "technique"
            }
            # Try to find a default based on the last part of the config key
            key_parts = config_key.split('.')
            last_part = key_parts[-1]
            return defaults.get(last_part, "element")
        return self.config.random.choice(choices)
