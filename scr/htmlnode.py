class HTMLNode:
    def __init__(self, Tag, Value, Children, Props) -> None:
        self.tag = Tag
        self.value = Value
        self.children = Children
        self.props = Props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        atr = ""
        for key,value in self.props.items():
            atr = atr + f" {key}={value}"
        
        return atr
    
    def __repr__(self) -> str:
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"