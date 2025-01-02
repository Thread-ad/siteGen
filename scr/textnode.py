from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "Normal text"
    BOLD_TEXT = "Bold text"
    ITALIC_TEXT = "Italic text"
    CODE_TEXT = "Code text"
    LINK = "Link"
    IMAGE = "Image"


class TextNode:
    def __init__(TEXT, TEXT_TYPE, URL):
        self.text + TEXT
        self.text_type = TEXT_TYPE
        self.url = URL


        def __eq__(self):
            return (
                self.text == self.text_type
                and self.text_type == self.url
            )



    