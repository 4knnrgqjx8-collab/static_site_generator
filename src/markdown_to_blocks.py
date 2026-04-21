def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block:
            new_blocks.append(block.strip())

    return new_blocks


