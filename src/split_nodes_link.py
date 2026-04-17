from textnode import TextNode, TextType
from extract_markdown_links import extract_markdown_links
import re

def split_nodes_link(node):
    if node.text_type.value in ["code", "images", "links"]:
        raise Exception('invalid text type')

    text = node.text
    list_of_links = extract_markdown_links(text)
    nodes = [] 
    for link in list_of_links:
        start = text.index(f"[{link[0]}]({link[1]})")
        if start != 0:
            nodes.append(TextNode(text[:start], node.text_type))
        nodes.append(TextNode(link[0], TextType.LINKS, link[1]))
        text = text[start+len(link[0]+link[1])+5:]

    if text:
        nodes.append(TextNode(text, node.text_type))

    return nodes


