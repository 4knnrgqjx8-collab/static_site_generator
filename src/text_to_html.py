from htmlnode import HTMLNode, LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception("text type not supported")
    
    elif text_node.text_type.value == "plain":
        return LeafNode(None, text_node.text)
    elif text_node.text_type.value == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type.value == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type.value == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type.value == "links":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type.value == "images":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

 
