class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        final_str = ""
        if self.props != None:
            for prop in self.props.keys():
                final_str += f' {prop}="{self.props[prop]}"'
        return final_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" 
   #надо ли выводить детей и свойства по-другому?#

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}>{self.props_to_html()}{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})" 

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is mandatory")
        if len(self.children) == 0:
            raise ValueError("A parent node must have children")
        fin_str = f"<{self.tag}>"
        for child in self.children:
            fin_str += child.to_html()
        return fin_str + f"</{self.tag}>"  
