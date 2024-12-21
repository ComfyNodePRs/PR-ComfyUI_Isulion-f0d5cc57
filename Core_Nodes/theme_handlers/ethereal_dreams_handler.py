from typing import Dict
from .base_handler import BaseThemeHandler

class EtherealDreamsThemeHandler(BaseThemeHandler):
    """Handler for ethereal dreams-themed prompt generation."""
    
    def generate(self, custom_subject: str = "",
                custom_location: str = "",
                include_environment: str = "yes",
                include_style: str = "yes",
                include_effects: str = "yes") -> Dict[str, str]:
        """Generate ethereal dreams-themed components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            components["subject"] = (
                f"((ethereal {custom_subject})), "
                f"((dreamlike)), ((surreal)), "
                f"((otherworldly appearance))"
            )
        else:
            subject = self._get_random_choice("ethereal_dreams.subjects")
            realm = self._get_random_choice("ethereal_dreams.realms")
            feature = self._get_random_choice("ethereal_dreams.features")
            components["subject"] = (
                f"((ethereal {subject} in {realm})), "
                f"((featuring {feature})), ((dreamlike)), "
                f"((surreal)), ((otherworldly appearance))"
            )
        
        # Generate environment if requested
        if include_environment == "yes":
            if custom_location:
                components["environment"] = (
                    f"in ((ethereal {custom_location})) with "
                    f"((dreamlike setting)), ((surreal space))"
                )
            else:
                setting = self._get_random_choice("ethereal_dreams.settings")
                element = self._get_random_choice("ethereal_dreams.elements")
                components["environment"] = (
                    f"in ((ethereal {setting})) with "
                    f"((dreamlike {element})), "
                    f"((surreal environment)), ((otherworldly atmosphere)), "
                    f"((ethereal realm))"
                )
        
        # Generate style if requested
        if include_style == "yes":
            style = self._get_random_choice("ethereal_dreams.styles")
            essence = self._get_random_choice("ethereal_dreams.essences")
            components["style"] = (
                f"((styled with {style} essence)), "
                f"((embodying {essence} quality)), "
                f"((ethereal artistry)), ((dreamlike aesthetic)), "
                f"((surreal beauty))"
            )
        
        # Generate effects if requested
        if include_effects == "yes":
            effect = self._get_random_choice("ethereal_dreams.effects")
            aura = self._get_random_choice("ethereal_dreams.auras")
            components["effects"] = (
                f"with ((ethereal {effect} effects)), "
                f"((dreamlike {aura} aura)), "
                f"((surreal atmosphere)), ((otherworldly ambiance))"
            )
        
        return components