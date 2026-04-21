from blocktype import BlockType, block_to_block_type
import unittest

class test_block_to_blocktype(unittest.TestCase):

    def test_standard(self):
        text = """```
        this is some code print("pimpirim")```"""
        self.assertEqual(BlockType.CODE, block_to_block_type(text))
        
        text = """### some header blablabla"""
        self.assertEqual(BlockType.HEADING, block_to_block_type(text))

        text = """- this is an
- unordered list
- I hope this works"""
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(text))

        text = """>a veeeery smart quote
>which is more than 1 line"""
        self.assertEqual(BlockType.QUOTE, block_to_block_type(text))

        text = """1. milk
2. bread
3. coconut
4. butter"""
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(text))

        text = "it's just a paragraph, nothing special"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

    def test_possible_fails(self):
        text = "######## thats a heading with 7 #"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = "``code that is not formated right```"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = """-no space for list
-do some pushups
-eat"""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = """>only one quote symbol in the multi-line quote
pimpirim"""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = """2. milk
5. vodka
7. pringles"""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))



