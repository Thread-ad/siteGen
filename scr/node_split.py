from textnode import TextNode, TextType



def split_nodes_deliminer(old_nodes, deliminer, text_type):
    new_nodes = []

    for node in old_nodes:

        if node.text_type.value != "Normal":
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