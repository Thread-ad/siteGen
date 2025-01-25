from htmlnode import HTMLNode, LeafNode, SovereignNode
from textnode import TextNode, TextType, text_node_to_html_node
from node_split import split_text, split_blocks, block_to_block_type


def SUPER_MEGA_markdown_to_html(everything):
    blocks = split_blocks(everything)
    Mega = []

    for block in blocks:
        srp = block.strip()
        if len(block) == 0:
            continue
        Mega.append(block_to_html(srp))

    return SovereignNode("div",Mega).to_html()
        

    

def block_to_html(block):
    html = ""
    match block_to_block_type(block):
        case "List" | "OList":
            html = SovereignNode(tagging(block), unlist(block))
  
        
        case "Code":
            html = SovereignNode(tagging(block), text_to_leaf(block))
  
        
        case "Heading":
            header = block[hashes(block)+1:]
            html = SovereignNode(tagging(block), text_to_leaf(header))

        case "Paragraph":
            html = SovereignNode(tagging(block), text_to_leaf(block))

        case "Quote":
            quote = block[2:]
            html = SovereignNode(tagging(block), text_to_leaf(quote))
    
    return html
        
        


def tagging(block):
    result = ""
    block_type = block_to_block_type(block)
    match block_type:
        case "Quote":
            result = "blockquote"
        
        case "List":
            result = "ul"
        
        case "OList":
            result = "ol"
        
        case "Code":
            result = "pre"
        
        case "Heading":
            result = f"h{hashes(block)}"

        case "Paragraph":
            result = "p"
            #print(f"TAG CHECK: {block} = {result}")
    return result
        
def hashes(block):
    x = 0
    for i in range(8):
        if block[i] == "#":
            x += 1
            continue
        else:
            return x
        
def unlist(input):
    result = []
    list = input.split("\n")
    for item in list:
        item = item.strip()
        leaf = item[2:]
        leaf = leaf.strip()
        leaves = text_to_leaf(leaf)
        
        result.append(SovereignNode("li",leaves))
    return result

def text_to_leaf(block):
    nodes = split_text(block)
    leaves = []
    for node in nodes:
        leaves.append(text_node_to_html_node(node))
    return leaves

