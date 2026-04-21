from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter
import re
from textnode import TextNode, TextType
def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.PLAIN)]
    char_to_char = {"**": TextType.BOLD,
                    "_": TextType.ITALIC,
                    "`": TextType.CODE,
                    "*": TextType.ITALIC}
    special_chars_presented = re.findall(r"\*{2}|[\*_`]", text)
    for special_char in special_chars_presented:
        new_nodes = split_nodes_delimiter(new_nodes, special_char,
                                         char_to_char[special_char])
        
    new_nodes = split_nodes_image(new_nodes)
    return split_nodes_link(new_nodes)



