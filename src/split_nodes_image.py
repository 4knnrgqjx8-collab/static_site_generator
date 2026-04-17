from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images
import re

def split_nodes_image(node):
    if node.text_type.value in ["code", "images", "links"]:
        raise Exception('invalid text type')
    text = node.text
    list_of_images = extract_markdown_images(text)
    nodes = []
    for im in list_of_images:
        start = text.index(f"![{im[0]}]({im[1]})")
        if start != 0:
            nodes.append(TextNode(text[:start], node.text_type))
        nodes.append(TextNode(im[0], TextType.IMAGES, im[1]))
        text = text[start+len(im[0]+im[1])+6:]

    if text:
        nodes.append(TextNode(text, node.text_type))

    return nodes

