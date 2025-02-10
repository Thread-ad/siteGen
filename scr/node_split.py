from textnode import TextNode, TextType
from functions import extract_images, extract_links


def split_text(text):
    text = text.strip()
    node = [TextNode(text, TextType.NORMAL_TEXT)]
    node = split_nodes_deliminer(node, "**", TextType.BOLD_TEXT)
    node = split_nodes_deliminer(node, "*", TextType.ITALIC_TEXT)
    node = split_nodes_deliminer(node, "```", TextType.CODE_TEXT)
    node = split_nodes_images(node)
    node = split_nodes_links(node)

    return node

def split_nodes_deliminer(old_nodes, deliminer, text_type):
    new_nodes = []

    for node in old_nodes:

        #node.text = node.text.strip()

        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        split = node.text.split(deliminer)
        if len(split) %2 == 0:
            print(f"FROM : {old_nodes}")
            print(f"Node: {node}")
            raise Exception("Indentation was not closed!")
        for i in range(len(split)):
            if i %2 == 0:
                split_nodes.append(TextNode(split[i], TextType.NORMAL_TEXT))
            else:
                split_nodes.append(TextNode(split[i], text_type))

        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_images(old_nodes):
    new_node = []
    image = ""
    split = []


    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_node.append(node)
            continue
        text = node.text
        image = extract_images(node.text)

        if image != []:
            for item in image:
                item_image = f"![{item[0]}]({item[1]})"
                split = text.split(item_image)
                new_node.append(TextNode(split[-2], TextType.NORMAL_TEXT))
                new_node.append(TextNode(item[0], TextType.IMAGE, item[1]))
                text = split[-1]
        else:
            new_node.append(TextNode(node.text, TextType.NORMAL_TEXT))
        if split != []:
            if split[-1] != "":
                new_node.append(TextNode(split[-1], TextType.NORMAL_TEXT))
    return new_node

def split_nodes_links(old_nodes):

    new_node = []
    link = ""
    split = []


    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_node.append(node)
            continue
        text = node.text
        link = extract_links(node.text)

        if link != []:
            for item in link:
                item_link = f"[{item[0]}]({item[1]})"
                split = text.split(item_link)
                new_node.append(TextNode(split[-2], TextType.NORMAL_TEXT))
                new_node.append(TextNode(item[0], TextType.LINK, item[1]))
                text = split[-1]
        else:
            new_node.append(TextNode(node.text, TextType.NORMAL_TEXT))
        if split != []:
            if split[-1] != "":
                new_node.append(TextNode(split[-1], TextType.NORMAL_TEXT))
    return new_node

def split_blocks(text):
    blocks = text.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


'''def split_blocks(text):
    list = []
    list_of_lists = []
    blocks = text.split("\n")
    for block in blocks:
        
        if block == "":
            continue
        block = block.strip()

        if block[0] == "*":
                list_of_lists.append(block)
        else:
            if list_of_lists != []:
                list.append("\n".join(list_of_lists))
                list_of_lists = []

            list.append(block)
    if list_of_lists != []:
        list.append("\n".join(list_of_lists))
    return list'''

def block_to_block_type(block):
    if len(block) == 0:
        return
    if heading_check(block):
        return "Heading"
    
    elif block[0:3] == "```" and block[-3:] == "```":
        return "Code"
    
    elif quote_check(block):
        return "Quote"
    
    elif list_check(block):
        return "List"
    
    elif ord_list_check(block):
        return "OList"
    
    else:
        return "Paragraph"


def heading_check(text):
    
    text = text.strip()
    if text[0] != "#":
        return False
    for i in range(8):
        if text[0] == "#":
            if text[i] == " ":
                return True
            elif text[i] == "#":
                continue
        
    return False
    
def quote_check(text):
    quotes = text.split("\n")
    for quote in quotes:
        if quote[0] == ">":
            continue
        else:
            return False
    return True

def list_check(text):
    lists = text.split("\n")
    for list in lists:
        list = list.strip()
        if list[0:2] == "* " or list[0:2] == "- ":
            continue
        else:
            return False
    return True

def ord_list_check(text):
    count = 0
    lists = text.split("\n")
    for list in lists:
        list = list.strip()
        if list[0:3] == str(count+1)+". ":
            count+=1
            continue
        else:
            return False
    return True