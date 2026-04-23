import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
from copy_dir import copy_dir

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as from_file:
        contents_from = from_file.read()
    with open(template_path, "r") as template_file:
        contents_template = template_file.read()
    
    html_string = markdown_to_html_node(contents_from).to_html()
    page_title = extract_title(contents_from)
    new_contents = contents_template.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(new_contents)

