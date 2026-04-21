from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images
import re

def split_nodes_image(nodes):
    new_nodes = []
    for node in nodes:
        if node.text_type.value in ["code", "images", "links"]:
            new_nodes.append(node)
        else:
            text = node.text
            list_of_images = extract_markdown_images(text)
            for im in list_of_images:
                start = text.index(f"![{im[0]}]({im[1]})")
                if start != 0:
                    new_nodes.append(TextNode(text[:start], node.text_type))
                new_nodes.append(TextNode(im[0], TextType.IMAGES, im[1]))
                text = text[start+len(im[0]+im[1])+5:]

            if text:
                new_nodes.append(TextNode(text, node.text_type))

    return new_nodes

