from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "Normal text"
    BOLD_TEXT = "Bold text"
    ITALIC_TEXT = "Italic text"
    CODE_TEXT = "Code text"
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



    