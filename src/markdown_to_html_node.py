from blocktype import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from htmlnode import ParentNode, LeafNode
from text_to_html import text_node_to_html_node
from blocktype import BlockType
import re

def blocktype_to_oldest_parent(block, blocktype):
    
    if blocktype.value == "heading":
        length = len(re.findall(r"^#{1,6} ", block)[0])
        block = block[length:]
        tag = f"h{length-1}"
        children = []
        for text_node in text_to_textnodes(block):
            children.append(text_node_to_html_node(text_node))
        return ParentNode(tag, children)

    elif blocktype.value == "code":
        return ParentNode("pre",[LeafNode("code", block[4:-3])])

    elif blocktype.value == "paragraph":
        children = []
        block = " ".join(block.split("\n"))
        for text_node in text_to_textnodes(block):
            children.append(text_node_to_html_node(text_node))
        return ParentNode("p", children)


    elif blocktype.value == "quote":
        new_block = block[2:].replace("\n> ", "\n").replace("\n>", "\n") if block.startswith("> ") else block[1:].replace("\n> ", "\n").replace("\n>", "\n")
        children = []
        for text_node in text_to_textnodes(new_block):
            children.append(text_node_to_html_node(text_node))
        return ParentNode("blockquote", children)

    elif blocktype.value == "unordered_list":
        new_block = block[2:].replace("\n- ", "\n")
        line_blocks = []
        for line in new_block.split("\n"):
            if not line:
                continue
            line = text_to_textnodes(line)
            if len(line) == 1 and line[0].text_type.value == "plain":
                line_blocks.append(LeafNode("li", line[0].text))
            else:
                nodes = []
                for node in line:
                    nodes.append(text_node_to_html_node(node))
                line_blocks.append(ParentNode("li", nodes))
        return ParentNode("ul", line_blocks)

    elif blocktype.value == "ordered_list":
        line_blocks = []
        for i, line in enumerate(block.split("\n"), start=1):
            if not line:
                continue
            line = line.replace(f"{i}. ", "", 1)
            line = text_to_textnodes(line)
            if len(line) == 1 and line[0].text_type.value == "plain":
                line_blocks.append(LeafNode("li", line[0].text))
            else:
                nodes = []
                for node in line:
                    nodes.append(text_node_to_html_node(node))
                line_blocks.append(ParentNode("li", nodes))
        return ParentNode("ol", line_blocks)


def markdown_to_html_node(text):
    blocks = markdown_to_blocks(text)
    children = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        children.append(blocktype_to_oldest_parent(block, blocktype))
    return ParentNode("div", children)

print(markdown_to_html_node("""
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""))
        
