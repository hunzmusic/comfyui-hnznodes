import torch
import numpy as np

class CombineChannelsGrayscale:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "channel": (["red", "green", "blue"], {"default": "red"}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("grayscale_image",)
    FUNCTION = "convert_to_grayscale"
    CATEGORY = "hnznodes/image"

    def convert_to_grayscale(self, image, channel):
        # Ensure image is a PyTorch tensor
        if not isinstance(image, torch.Tensor):
            raise TypeError("Input 'image' must be a PyTorch tensor.")

        # Handle potential batch dimension (or lack thereof)
        if image.ndim == 3:  # Single image (HWC)
            image = image.unsqueeze(0)  # Add batch dimension (BHWC)
        elif image.ndim != 4:  # (B)HWC
            raise ValueError("Input 'image' must be a 3D (HWC) or 4D (BHWC) tensor.")

        batch_size, height, width, channels = image.shape

        if channels < 3:  # input could be grayscale
            image = image.repeat(1, 1, 1, 3)  # Expand to have at least 3 channels (even if already grayscale!)
            channels = 3 # now we have 3 channels
        
        # Mapping from string to channel index
        channel_map = {"red": 0, "green": 1, "blue": 2}
        channel_index = channel_map[channel]

        # Extract the selected channel
        selected_channel = image[:, :, :, channel_index:channel_index+1]

        # Repeat the selected channel across all three output channels
        grayscale_image = selected_channel.repeat(1, 1, 1, 3)

        return (grayscale_image,)

# --- Node definition for ComfyUI ---
NODE_CLASS_MAPPINGS = {
    "CombineChannelsGrayscale": CombineChannelsGrayscale
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CombineChannelsGrayscale": "Combine Channels Grayscale"
}