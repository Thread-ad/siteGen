import unittest
from textnode import TextNode, TextType
from node_split import split_nodes_deliminer


class TestInlineMarkdown(unittest.TestCase):
    

    def test_input(self):
        node2 = TextNode("This is *bold* text", TextType.NORMAL_TEXT)
        del_array = split_nodes_deliminer([node2], "*", TextType.BOLD_TEXT)
        self.assertEqual(del_array, [
            TextNode("This is ", TextType.NORMAL_TEXT), 
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" text", TextType.NORMAL_TEXT)
        ])

    def test_multiple_dels(self):
        node = TextNode("This node has *bold text* and **italic text** in it.", TextType.NORMAL_TEXT)
        result = split_nodes_deliminer([node], "**", TextType.ITALIC_TEXT)
        self.assertEqual(
                result, 
            [
                TextNode("This node has *bold text* and ",TextType.NORMAL_TEXT),
                TextNode("italic text", TextType.ITALIC_TEXT),
                TextNode(" in it.", TextType.NORMAL_TEXT)
            ]
        )
        self.assertEqual(
            split_nodes_deliminer(result, "*", TextType.BOLD_TEXT),
            [
                TextNode("This node has ", TextType.NORMAL_TEXT),
                TextNode("bold text", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode("italic text", TextType.ITALIC_TEXT),
                TextNode(" in it.", TextType.NORMAL_TEXT)
            ]
        )

    def test_multiple_same_dels(self):
        node = TextNode("This text has **Bold text** and **Bold text** in it.", TextType.NORMAL_TEXT)
        result = split_nodes_deliminer([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(
            result,
            [
                TextNode("This text has ", TextType.NORMAL_TEXT),
                TextNode("Bold text", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode("Bold text", TextType.BOLD_TEXT),
                TextNode(" in it.", TextType.NORMAL_TEXT)                
            ]
        )


if __name__ == "__main__":
    unittest.main()
