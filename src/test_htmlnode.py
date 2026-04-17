import unittest                                                                                       
                                                                                                      
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        html_node = HTMLNode()
        self.assertRaises(NotImplementedError, html_node.to_html)

    def test_repr(self):
        html_node = HTMLNode("p", "this is the text", [HTMLNode("a", "also text"),
                                                     HTMLNode("a", "another text")],
                             {"href": "https://www.google.com"})
        self.assertEqual(repr(html_node), f"HTMLNode({html_node.tag}, {html_node.value}, {html_node.children}, {html_node.props})" )

    def test_props_to_html(self):
        html_node = HTMLNode("p", "this is the text", [HTMLNode("a", "also text"),
                                                     HTMLNode("a", "another text")],
                             {"href": "https://www.google.com"})
        self.assertEqual(html_node.props_to_html(), ' href="https://www.google.com"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_def_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.children, None)

    def test_no_val_error(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_repr(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(repr(node), f"HTMLNode({node.tag}, {node.value}, {node.props})")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_def_value(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.value, None)

    def test_no_children(self):
        parent_node = ParentNode("b", [])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_no_tag(self):        
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

