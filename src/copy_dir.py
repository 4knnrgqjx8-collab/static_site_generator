import os
import shutil

def copy_dir(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for content in os.listdir(source):
        path_content = os.path.join(source, content)
        if os.path.isfile(path_content):
            shutil.copy(path_content, dest)
        else:
            new_dest = os.path.join(dest, content)
            copy_dir(path_content, new_dest)




        
        

