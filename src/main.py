from copy_dir import copy_dir
from generate_pages_recursive import generate_pages_recursive
import sys
def main(src, dst):
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    copy_dir(src, dst)
    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath
            )   
    
main("static", "docs")

