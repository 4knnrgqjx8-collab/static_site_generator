import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class test_split_nodes_delimiter(unittest.TestCase):
    def test_plain_text(self):
        node = TextNode("This is text without any insertions", TextType.PLAIN)
        desired_result = [TextNode(node.text, node.text_type)]
        real_result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(desired_result, real_result)

    def test_italic_text(self):
        node = TextNode("This is text with _italiano_ text", TextType.PLAIN)
        desired_result = [TextNode("This is text with ", TextType.PLAIN), 
                          TextNode("italiano", TextType.ITALIC), 
                          TextNode(" text", TextType.PLAIN)]
        real_result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(desired_result, real_result)

    def test_bold_text(self):
        node = TextNode("This is text with a **bold** text", TextType.PLAIN)
        desired_result = [TextNode("This is text with a ", TextType.PLAIN), 
                          TextNode("bold", TextType.BOLD), 
                          TextNode(" text", TextType.PLAIN)]
        real_result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(desired_result, real_result)

    def test_unmatched_delimiter(self):
        node = TextNode("This is text with **bold unmatched delimiter", TextType.PLAIN)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "**", TextType.BOLD)

    def test_all_code(self):
        node = TextNode("```this is code```", TextType.PLAIN)
        desired_result = [TextNode("this is code", TextType.CODE)]
        real_result = split_nodes_delimiter([node], "```", TextType.CODE)
        self.assertEqual(desired_result, real_result)

    def test_two_blocks(self):
        
        node = TextNode("This is text with a **bold** text and **another bold text** pupupu", 
                        TextType.PLAIN)
        desired_result = [TextNode("This is text with a ", TextType.PLAIN), 
                          TextNode("bold", TextType.BOLD), 
                          TextNode(" text and ", TextType.PLAIN), 
                          TextNode("another bold text", TextType.BOLD), 
                          TextNode(" pupupu", TextType.PLAIN)]
        real_result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(desired_result, real_result)









