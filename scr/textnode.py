from enum import Enum
from htmlnode import HTMLNode, LeafNode


class TextType(Enum):
    NORMAL_TEXT = "Normal"
    BOLD_TEXT = "Bold"
    ITALIC_TEXT = "Italic"
    CODE_TEXT = "Code"
    LINK = "Link"
    IMAGE = "Image"


class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL


    def __eq__(self,other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
            )
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}"
    
def text_node_to_html_node(self):
    match self.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(None,self.text)
            
        case TextType.BOLD_TEXT:
            return LeafNode("b",self.text)
            
        case TextType.ITALIC_TEXT:
            return LeafNode("i",self.text)

        case TextType.CODE_TEXT:
            return LeafNode("code",self.text)   

        case TextType.LINK:
            return LeafNode("a", self.text, {"href":self.url })

        case TextType.IMAGE:
            return LeafNode("img", "", {"scr":self.url,"alt":self.text})


    pass