class HTMLNode:
    def __init__(self, Tag=None, Value=None, Children=None, Props=None) -> None:
        self.tag = Tag
        self.value = Value
        self.children = Children
        self.props = Props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        atr = ""
        for key,value in self.props.items():
            atr = atr + f' {key}="{value}"'        
        return atr
    
    def __repr__(self) -> str:
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, Tag=None, Value=None, Props=None):
        super().__init__(Tag, Value,None, Props)

    def __repr__(self) -> str:
        return super().__repr__()

    def props_to_html(self):
        return super().props_to_html()

    def to_html(self):
        if self.value == None:
            raise ValueError ("Must have a value")
        
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, Tag, Children, Props=None) -> None:
        super().__init__(Tag, None, Children, Props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Must have a tag")
        if self.children == None:
            raise ValueError("Must have a cild class")
        
        ext_str = f"<{self.tag}>"

        for child in self.children:
            ext_str = ext_str + child.to_html()
        return ext_str + f"</{self.tag}>"

