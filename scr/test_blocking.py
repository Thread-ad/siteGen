import unittest
from node_split import split_text,split_blocks
from textnode import TextNode, TextType


class TestBlockedMarkdown(unittest.TestCase):


    def test_blocking(self):
        raw = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''
        self.assertEqual(
            split_blocks(raw),
            ["# This is a heading",
             "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
             ]
        )

    def test_gen_block(self):
        raw = '''# Heading 1

This is a paragraph with **bold** and *italic* text.

* This is the first list item
* This is the second list item
* This is the third list item

This is another paragraph without any special formatting.

## Heading 2

Here's a second heading with another paragraph below.

* List items continue here
* Another list item in a separate block'''

        self.assertEqual(
            split_blocks(raw),
            [
             "# Heading 1",
             "This is a paragraph with **bold** and *italic* text.",
             "* This is the first list item\n* This is the second list item\n* This is the third list item",
            "This is another paragraph without any special formatting.",
            "## Heading 2",
            "Here's a second heading with another paragraph below.",
            "* List items continue here\n* Another list item in a separate block"
            ]
        )

