from markdown_to_blocks import markdown_to_blocks
import unittest


class test_markdown_to_blocks(unittest.TestCase):
    def test_standard(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        self.assertListEqual(["# This is a heading",
                              "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                              "- This is the first list item in a list block\n- This is a list item\n- This is another list item"], markdown_to_blocks(text))

    def test_with_empty(self):
        text = """Now there'll be an **empty** line



        some more text"""
        self.assertListEqual(["Now there'll be an **empty** line", "some more text"],
                             markdown_to_blocks(text))

    def test_no_text(self):
        text = ""
        self.assertListEqual([], markdown_to_blocks(text))
