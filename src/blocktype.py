from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(text):
    counter = 0 
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    elif text.startswith("```\n") and text[-3:] == "```":
        return BlockType.CODE

    ordered_list_marker = True
    unordered_list_marker = True
    quote_marker = True
    for line in text.split("\n"):
        counter += 1
        if not line.startswith("- "):
            unordered_list_marker = False
        if not line.startswith(">"):
            quote_marker = False
        if not line.startswith(f"{counter}. "):
            ordered_list_marker = False

    if quote_marker:
        return BlockType.QUOTE
    
    elif unordered_list_marker:
        return BlockType.UNORDERED_LIST

    elif ordered_list_marker:
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH

