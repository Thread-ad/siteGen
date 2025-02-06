import unittest
from node_split import split_text,split_blocks, block_to_block_type
from textnode import TextNode, TextType


class TestBlockedMarkdown(unittest.TestCase):


    def test_split_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = split_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = split_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), "Heading")
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), "Code")
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), "Quote")
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), "List")
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), "OList")
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), "Paragraph")

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

    def test_block_type(self):
        raw = """# Sample Markdown Text

This is a paragraph with some **bold** and *italic* text. Markdown allows easy formatting for documents. Below, you'll see various types of content.

## Code Block

Here is a Python code block:

```python
def greet(name):
    return f"Hello, {name}!"
print(greet("World"))```

> "In the middle of every difficulty lies opportunity." – Albert Einstein

## Unordered List

* Coffee
* Tea
* Juice

## Ordered List

1. Wake up early
2. Brush your teeth
3. Have breakfast
4. Start your day

"""

        self.assertEqual(
            temp(raw), [
                "Heading",
                "Paragraph",
                "Heading",
                "Paragraph",
                "Code",
                "Quote",
                "Heading",
                "List",
                "Heading",
                "OList",

            ]
        )

def temp(txt):
    blocks = split_blocks(txt)
    result = []
    for block in blocks:
        result.append(block_to_block_type(block))


    return result


