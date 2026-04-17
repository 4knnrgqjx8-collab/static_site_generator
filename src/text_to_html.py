from htmlnode import HTMLNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception("text type not supported")
    
    elif text_node.text_type.value == "plain":
        return HTMLNode(None, text_node.text)
    elif text_node.text_type.value == "bold":
        return HTMLNode("b", text_node.text)
    elif text_node.text_type.value == "code":
        return HTMLNode("code", text_node.text)
    elif text_node.text_type.value == "italic":
        return HTMLNode("i", text_node.text)
    elif text_node.text_type.value == "links":
        return HTMLNode("a", text_node.text, None, {"href": text_node.url})
    elif text_node.text_type.value == "images":
        return HTMLNode("img", None , None, {"src": text_node.url, "alt": text_node.text})


   
