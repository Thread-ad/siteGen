import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    '''#Html class print property test
    def test_prnt(self):

        dict1 = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        dict2 = {
            "look": "ok",
            "brazen": "look",
            "hirearchy":"looking good"
        }
        dict3 = {
            "just me": "exists"
        }
        
        property1 = HTMLNode("hello",None,None,dict1)
        property2 = HTMLNode(None,None,None,dict2)
        property3 = HTMLNode(None,None,None,dict3)

        print(f"{property1.props_to_html()}\n{property2.props_to_html()}\n{property3.props_to_html()}")
'''

    '''#Leaf class to_html test
    def test_to_html(self):
        greeting = LeafNode("p","I greet you!")
        print(greeting.to_html())

        no_tag = LeafNode(None,"I'm tagless")
        print(no_tag.to_html())

        no_value = LeafNode("g","Click here!",{"href": "https://www.google.com"})
        print(no_value.to_html())
'''

    '''#test print parent and nested nodes
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
        )
        print(f"{node.to_html()}")
    '''

    #def test_text_node_to_html_node(self):

if __name__ == "__main__":
    unittest.main()
