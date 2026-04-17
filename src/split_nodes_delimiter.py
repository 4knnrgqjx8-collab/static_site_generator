from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for origin_node in old_nodes:
        if origin_node.text_type.value != "plain":
            new_nodes.append(origin_node)
        else:
            while delimiter in origin_node.text:
                start_index = origin_node.text.index(delimiter)
                if start_index != 0:
                    new_nodes.append(TextNode(origin_node.text[:start_index], TextType.PLAIN))
                origin_node.text = origin_node.text[start_index+len(delimiter):]
                try:
                    close_index = origin_node.text.index(delimiter)
                except Exception:
                    raise Exception("unmatched delimiters were found")
                new_nodes.append(TextNode(origin_node.text[:close_index], text_type))
                origin_node.text = origin_node.text[close_index+len(delimiter):]

            if len(origin_node.text) != 0:
                new_nodes.append(TextNode(origin_node.text, TextType.PLAIN))


    ##or proto_nodes = origin_node.text.split(delimiter)
        #if len(proto_nodes) % 2 == 0:
            #raise Exception("unmatched delimiters")
        #for i in range(len(proto_nodes)):
        #    if len(proto_nodes[i]) != 0:
        #        if i % 2 != 0:
        #            new_nodes.append(TextNode(proto_nodes[i], text_type))
        #        else:
        #            new_nodes.append(TextNode(proto_nodes[i], TextType.PLAIN))

            
    
    return new_nodes
