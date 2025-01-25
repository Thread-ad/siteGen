import unittest
from htmlnode import *
from block_to_html import SUPER_MEGA_markdown_to_html

class TestMarkdownToHTML(unittest.TestCase):


    def test_single_paragraph(self):
        markdown = "This is a simple paragraph."
        expected_html = "<div><p>This is a simple paragraph.</p></div>"
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html)

    def test_heading(self):
        markdown = "# This is a Heading 1"
        expected_html = "<div><h1>This is a Heading 1</h1></div>"
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html)

    def test_subheading(self):
        markdown = "## This is a Heading 2"
        expected_html = "<div><h2>This is a Heading 2</h2></div>"
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html)

    def test_bold_text_in_paragraph(self):
        markdown = "This is **bold** text."
        expected_html = "<div><p>This is <b>bold</b> text.</p></div>"
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html)

    def test_italic_text_in_paragraph(self):
        markdown = "This is *italic* text."
        expected_html = "<div><p>This is <i>italic</i> text.</p></div>"
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html)

    def test_unordered_list(self):
        markdown = """

        - Item 1
        - Item 2
        - Item 3
        
        """
        expected_html = "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html)

    def test_ordered_list(self):
        markdown = """

        1. First item
        2. Second item
        3. Third item

        """
        expected_html = "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>"
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html)

    def test_code_block(self):
        markdown = """
        `python
        def hello_world():
            print(&quotHello, World!&quot)
        `
        """
        expected_html = "<div><pre><code>def hello_world():print(&quot;Hello, World!&quot;)</code></pre></div>"
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html)

    def test_quote_block(self):
        markdown = """
        > This is a quote block.
        """
        expected_html = "<div><blockquote>This is a quote block.</blockquote></div>"
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html)

    def test_mixed_content(self):
        markdown = """
        # Heading 1


        This is a paragraph with **bold** text and *italic* text.

        
        - First list item
        - Second list item

        
        > This is a blockquote.
        
        
        `python
        print("Code block!")
        `
        """
        expected_html = """
        <div><h1>Heading 1</h1><p>This is a paragraph with <strong>bold</strong> text and <em>italic</em> text.</p><ul><li>First list item</li><li>Second list item</li></ul><blockquote>This is a blockquote.</blockquote><pre><code>print(&quot;Code block!&quot;)</code></pre></div>
        """
        self.assertEqual(SUPER_MEGA_markdown_to_html(markdown), expected_html.strip())

if __name__ == '__main__':
    unittest.main()