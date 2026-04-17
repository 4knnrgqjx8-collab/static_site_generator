from textnode import TextNode, Bender

def main(text, text_type, url):
    return TextNode(text, text_type, url)

print(main("This is some anchor text", "link", "https://www.boot.dev"))
