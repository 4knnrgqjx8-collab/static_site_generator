import unittest
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode

class Test_text_to_html(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINKS, "this_is_a_link.com")
        transformed = text_node_to_html_node(node)
        self.assertEqual(transformed.tag, "a")
        self.assertEqual(transformed.value, "This is a link node") 
        self.assertEqual(transformed.props, {"href": node.url})

    def test_image(self):
        node = TextNode("This is the description", TextType.IMAGES, "this_is_a_source.com")
        transformed = text_node_to_html_node(node)
        self.assertEqual(transformed.tag, "img")
        self.assertEqual(transformed.props, {"src": node.url, "alt": node.text})

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")




