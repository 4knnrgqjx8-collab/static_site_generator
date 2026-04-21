import unittest
from split_nodes_link import split_nodes_link
from split_nodes_image import split_nodes_image
from textnode import TextType, TextNode

class test_split_nodes_link(unittest.TestCase):
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.PLAIN,
    )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
            TextNode("This is text with an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN),
            TextNode(
                "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
            ),
            ],
                new_nodes,
                )

    def test_split_im_wrongtype(self):
        node = TextNode("image", TextType.IMAGES, "hhttps://some_picture_site/picture345.MPEG")
        self.assertListEqual([node], split_nodes_link([node]))
        
    def test_split_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.PLAIN)
        self.assertListEqual([TextNode("This is text with a link ", TextType.PLAIN), 
                              TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"), 
                              TextNode(" and ", TextType.PLAIN), 
                              TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")], split_nodes_link([node]))

    def test_split_link_wrongtype(self):
        node = TextNode("```THIS IS ACTUALLY CODE```", TextType.CODE)
        self.assertListEqual([node], split_nodes_link([node]))






