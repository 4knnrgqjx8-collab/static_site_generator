from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType
import unittest

class test_text_to_textnodes(unittest.TestCase):

    def test_standard(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual([
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
                ], text_to_textnodes(text))


    def image_wrapped(self):
        text = "I wanna test the behavior with both *italic and ![image](https://some_site.com/some_picture.PNG)*"
        self.assertListEqual([TextNode("I wanna test the behavior with both ", TextType.PLAIN), 
                              TextNode("italic and ", TextType.ITALIC), 
                              TextNode("image", TextType.IMAGES, "https://some_site.com/some_picture.PNG")], text_to_textnodes(text))

    def one_by_one(self):
        text = "**bold**`code`[link](https://some_link.com)![image](https://some_site.com/some_picture.PNG) then some text"
        self.assertListEqual([TextNode("bold", TextType.BOLD), 
                              TextNode("code", TextType.CODE), 
                              TextNode("link", TextType.LINKS, "https://some_link.com"),
                              TextNode("image", TextType.IMAGES, "https://some_site.com/some_picture.PNG"), 
                              TextNode(" then some text", TextType.PLAIN)], text_to_textnodes(text))



