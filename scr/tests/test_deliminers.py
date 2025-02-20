import unittest
from htmlnode import *
from textnode import TextNode, TextType
from node_split import split_nodes_deliminer, split_nodes_images, split_nodes_links, split_text


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

    def test_extract_images(self):
        node = [
            TextNode(
    "Here is the official logo of Python: ![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png).",
    TextType.NORMAL_TEXT
    ),
            TextNode(
    "And this is the famous GitHub Octocat: ![GitHub Octocat](https://github.githubassets.com/images/modules/logos_page/Octocat.png).",
    TextType.NORMAL_TEXT
            )
        ]

        self.assertEqual(
            split_nodes_images(node),
        [
            TextNode("Here is the official logo of Python: ", TextType.NORMAL_TEXT),
            TextNode("Python Logo", TextType.IMAGE, "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"),
            TextNode(".", TextType.NORMAL_TEXT),
            TextNode("And this is the famous GitHub Octocat: ", TextType.NORMAL_TEXT),
            TextNode("GitHub Octocat", TextType.IMAGE, "https://github.githubassets.com/images/modules/logos_page/Octocat.png"),
            TextNode(".", TextType.NORMAL_TEXT)
        ]
        )
        

    def test_extract_links(self):
        node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.NORMAL_TEXT)
        split_nodes_links([node])

        node = [
            TextNode("Check out the [official Python website](https://www.python.org) for documentation and updates.", TextType.NORMAL_TEXT), 
            TextNode("If you're interested in open-source projects, explore repositories on [GitHub](https://github.com).", TextType.NORMAL_TEXT)
        ]
        self.assertEqual(
            split_nodes_links(node),
            [
                TextNode("Check out the ", TextType.NORMAL_TEXT),
                TextNode("official Python website", TextType.LINK, "https://www.python.org"),
                TextNode(" for documentation and updates.", TextType.NORMAL_TEXT),
                TextNode("If you're interested in open-source projects, explore repositories on ", TextType.NORMAL_TEXT),
                TextNode("GitHub", TextType.LINK, "https://github.com"),
                TextNode(".", TextType.NORMAL_TEXT)
                ]
        )

    def test_no_links(self):
        node = TextNode("Text with no link.", TextType.NORMAL_TEXT)

        self.assertEqual(
            split_nodes_links([node]),
            [
                TextNode("Text with no link.", TextType.NORMAL_TEXT)
            ]
        )

    def test_final_split(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)."
        self.assertEqual(
            split_text(text),
            [
                TextNode("This is ", TextType.NORMAL_TEXT),
                TextNode("text", TextType.BOLD_TEXT),
                TextNode(" with an ", TextType.NORMAL_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
                TextNode(" word and a ", TextType.NORMAL_TEXT),
                TextNode("code block", TextType.CODE_TEXT),
                TextNode(" and an ", TextType.NORMAL_TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL_TEXT), 
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(".", TextType.NORMAL_TEXT)
            ]
        )
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = SovereignNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = SovereignNode("span", [grandchild_node])
        parent_node = SovereignNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = SovereignNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = SovereignNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()

