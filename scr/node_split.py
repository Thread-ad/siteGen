from textnode import TextNode, TextType
from functions import extract_images, extract_links


def split_text(text):
    node = TextNode(text, TextType.NORMAL_TEXT)
    node = split_nodes_deliminer([node], "**", TextType.BOLD_TEXT)
    node = split_nodes_deliminer(node, "*", TextType.ITALIC_TEXT)
    node = split_nodes_deliminer(node, "`", TextType.CODE_TEXT)
    node = split_nodes_images(node)
    node = split_nodes_links(node)

    return node

def split_nodes_deliminer(old_nodes, deliminer, text_type):
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
        else:
            split = node.text.split(deliminer)
            if len(split) %2 == 0:
                raise Exception("Indentationwas not closed!")
            for i in range(len(split)):
                if i %2 == 0:
                    new_nodes.append(TextNode(split[i], TextType.NORMAL_TEXT))
                else:
                    new_nodes.append(TextNode(split[i], text_type))

    
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
    return list
