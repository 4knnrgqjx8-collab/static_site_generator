from copy_dir import copy_dir
from generate_pages_recursive import generate_pages_recursive
import sys
def main(src, dst):
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    copy_dir("." + basepath+src, "." + basepath+dst)
    generate_pages_recursive("." + basepath + "content", "." + basepath + "template.html", "." + basepath + "docs", basepath)    
    
main("static", "docs")

