from copy_dir import copy_dir
from generate_pages_recursive import generate_pages_recursive
def main(src, dst):
    copy_dir(src, dst)
    generate_pages_recursive("./content", "template.html", "./public")    
main("static", "public")

