def extract_title(text):
    if text.find("# ") == -1:
        raise Exception("the file doesn't have a title")
    return text.split("\n\n")[0]


