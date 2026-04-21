from textnode import TextNode, TextType
from extract_markdown_links import extract_markdown_links
import re

def split_nodes_link(nodes):
    new_nodes = [] 
    for node in nodes:
        if node.text_type.value in ["code", "images", "links"]:
            new_nodes.append(node)
        else:
            text = node.text
            list_of_links = extract_markdown_links(text)
            for link in list_of_links:
                start = text.index(f"[{link[0]}]({link[1]})")
                if start != 0:
                    new_nodes.append(TextNode(text[:start], node.text_type))
                new_nodes.append(TextNode(link[0], TextType.LINKS, link[1]))
                text = text[start+len(link[0]+link[1])+4:]

            if text:
                new_nodes.append(TextNode(text, node.text_type))

    return new_nodes


