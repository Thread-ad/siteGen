import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
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