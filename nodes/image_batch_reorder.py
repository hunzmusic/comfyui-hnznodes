import torch
import random

class ImageBatchReorder:
    """
    Reorders a batch of images according to a specified order.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),  # Input image batch
                "order_type": (
                    [
                        "sequential",
                        "reverse",
                        "shuffle",
                        "custom",  # Added "custom" option
                        "rotate_right", #Shift elements to the right, with the last element wrapping around to the beginning
                        "rotate_left", #Shift elements to the left, with the first element wrapping around to the end.
                    ],
                    {
                        "default": "sequential"
                    }
                ),
                "custom_order": ("STRING", {  # Input for custom order indices
                    "multiline": True,  # Allows multiple lines for easier input
                    "default": "0,1,2,3"  # Default order (assuming batch size of 4)
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("reordered_images",)
    FUNCTION = "reorder_batch"
    CATEGORY = "hnznodes/image"

    def reorder_batch(self, images, order_type, custom_order, seed):
        # Get batch size
        batch_size = images.size(0)

        # Generate order indices based on order_type
        if order_type == "sequential":
            order = list(range(batch_size))
        elif order_type == "reverse":
            order = list(range(batch_size - 1, -1, -1))
        elif order_type == "shuffle":
            order = list(range(batch_size))
            rng = random.Random(seed)  # Use a random number generator with the seed
            rng.shuffle(order)
        elif order_type == "custom":
            try:
                # Parse the custom order string.  Handle different separators.
                order_str = custom_order.replace(" ", ",").replace(";", ",")  # Allow spaces, commas, semicolons
                order = [int(i.strip()) for i in order_str.split(",") if i.strip()]  # Convert to integers, handle empty entries

                # Validate custom order: Check length and index range
                if len(order) != batch_size:
                    raise ValueError(f"Custom order length ({len(order)}) must match batch size ({batch_size}).")
                if not all(0 <= i < batch_size for i in order):
                    raise ValueError(f"Custom order indices must be within the range of the batch size (0-{batch_size - 1}).")

            except ValueError as e:
                print(f"Error parsing custom order: {e}.  Using original order.")
                order = list(range(batch_size))  # Fallback to original order
        elif order_type == "rotate_right":
            order = [(i - 1) % batch_size for i in range(batch_size)]
        elif order_type == "rotate_left":
            order = [(i + 1) % batch_size for i in range(batch_size)]


        else:  # Should never happen, but good practice to have a default
            order = list(range(batch_size))

        # Reorder the images using torch.index_select
        reordered_images = torch.index_select(images, 0, torch.tensor(order, device=images.device))

        return (reordered_images,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ImageBatchReorder": ImageBatchReorder
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageBatchReorder": "Reorder Image Batch"
}