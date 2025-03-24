from .nodes.image_batch_reorder import NODE_CLASS_MAPPINGS as reorder_mappings, NODE_DISPLAY_NAME_MAPPINGS as reorder_names
from .nodes.combine_channels_grayscale import NODE_CLASS_MAPPINGS as combine_mappings, NODE_DISPLAY_NAME_MAPPINGS as combine_names
from .nodes.maleCharacter import NODE_CLASS_MAPPINGS as male_character, NODE_DISPLAY_NAME_MAPPINGS as character

NODE_CLASS_MAPPINGS = {**reorder_mappings, **combine_mappings, **male_character}
NODE_DISPLAY_NAME_MAPPINGS = {**reorder_names, **combine_names, **character}


__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']