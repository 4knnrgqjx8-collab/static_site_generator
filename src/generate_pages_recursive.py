import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
from copy_dir import copy_dir
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.isfile(dir_path_content):
        if dir_path_content.endswith(".md"):
            generate_page(dir_path_content, template_path, os.path.join(os.path.split(dest_dir_path)[0], os.path.split(dest_dir_path)[1].replace(".md", ".html")), basepath)
        return

    for entry in os.listdir(dir_path_content):
        generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry), basepath)


    

