import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_txt_to_html(self):
        text = TextNode("This is the text", TextType.BOLD_TEXT)
        test_leaf = text.text_node_to_html_node()
        print(f"{test_leaf.to_html()}")



if __name__ == "__main__":
    unittest.main()
