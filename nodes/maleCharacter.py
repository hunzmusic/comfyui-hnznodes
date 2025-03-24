import random

class MaleCharacterPromptGenerator:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "eye_color": (["Blue", "Brown", "Green", "Hazel", "Gray", "Black", "Random"],),
                "body_type": (["Slim", "Athletic", "Muscular", "Average", "Large", "Random"],),
                "race": (["White", "Black", "Asian", "Hispanic/Latino", "Native American", "Pacific Islander", "Mixed", "Random"],),
                "hair_color": (["Brown", "Black", "Blonde", "Red", "Gray", "White", "Random"],),
                "hair_style": (["Short", "Medium", "Long", "Bald", "Buzzcut", "Crew Cut", "Curly", "Wavy", "Random"],),
                "facial_hair": (["None", "Beard", "Goatee", "Mustache", "Sideburns", "Random"],),
                "clothing_style": (["Casual", "Formal", "Business", "Sporty", "Streetwear", "Random"],),
                "age_group": (["Young Adult (18-25)", "Adult (26-40)", "Middle-Aged (41-60)", "Senior (61+)", "Random"],),
                "expression": (["Neutral", "Smiling", "Frowning", "Serious", "Angry", "Surprised", "Random"],),
                "pose": (["Standing", "Sitting", "Walking", "Running", "Action Pose", "Random"],),
                "background_setting": (["Plain", "Urban", "Nature", "Indoors", "Fantasy", "Random"],),
                "additional_notes": ("STRING", {"multiline": True}),
                "randomize": (["Off", "On"],),  # Randomization switch
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}), # Random seed input

            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "hnznodes/prompt"

    def generate_prompt(self, eye_color, body_type, race, hair_color, hair_style, facial_hair, clothing_style, age_group, expression, pose, background_setting, additional_notes, randomize, seed):

        if randomize == "On":
            # Use the provided seed for reproducibility
            random.seed(seed)

            # Randomly select from each dropdown's options (excluding "Random" itself)
            eye_color = random.choice([opt for opt in self.INPUT_TYPES()["required"]["eye_color"][0] if opt != "Random"])
            body_type = random.choice([opt for opt in self.INPUT_TYPES()["required"]["body_type"][0] if opt != "Random"])
            race = random.choice([opt for opt in self.INPUT_TYPES()["required"]["race"][0] if opt != "Random"])
            hair_color = random.choice([opt for opt in self.INPUT_TYPES()["required"]["hair_color"][0] if opt != "Random"])
            hair_style = random.choice([opt for opt in self.INPUT_TYPES()["required"]["hair_style"][0] if opt != "Random"])
            facial_hair = random.choice([opt for opt in self.INPUT_TYPES()["required"]["facial_hair"][0] if opt != "Random"])
            clothing_style = random.choice([opt for opt in self.INPUT_TYPES()["required"]["clothing_style"][0] if opt != "Random"])
            age_group = random.choice([opt for opt in self.INPUT_TYPES()["required"]["age_group"][0] if opt != "Random"])
            expression = random.choice([opt for opt in self.INPUT_TYPES()["required"]["expression"][0] if opt != "Random"])
            pose = random.choice([opt for opt in self.INPUT_TYPES()["required"]["pose"][0] if opt != "Random"])
            background_setting = random.choice([opt for opt in self.INPUT_TYPES()["required"]["background_setting"][0] if opt != "Random"])
            # additional_notes = ""  # Removed: Now we *do* use the multiline input

        prompt_parts = []

        # Build the prompt string (same logic as before, but now using the potentially randomized values)
        prompt_parts.append("Male,")
        prompt_parts.append(age_group + ",")
        prompt_parts.append(race + ",")
        prompt_parts.append(body_type + " build,")
        prompt_parts.append(hair_color + " " + hair_style + " hair,")
        if facial_hair != "None":
            prompt_parts.append(facial_hair + ",")
        prompt_parts.append(eye_color + " eyes,")
        prompt_parts.append(expression + " expression,")
        prompt_parts.append("wearing " + clothing_style + " clothing,")
        prompt_parts.append(pose + ",")
        prompt_parts.append("background: " + background_setting)


        # Join the parts (same as before).
        base_prompt = " ".join(prompt_parts)

        # Always add additional notes
        if additional_notes.strip():  # Check if additional_notes is not just whitespace
             full_prompt = f"{base_prompt}, {additional_notes}"
        else:
             full_prompt = base_prompt


        return (full_prompt,)

# --- Node Definition for ComfyUI --- (No changes here)
NODE_CLASS_MAPPINGS = {
    "MaleCharacterPromptGenerator": MaleCharacterPromptGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MaleCharacterPromptGenerator": "Male Character Prompt"
}