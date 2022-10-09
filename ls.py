import os
import datetime as dt
from operator import attrgetter


class Item:
    
    def __init__(self, permissions, modtime, size, name, isdir):
        self.permissions = permissions
        self.modtime = modtime
        self.size = size
        self.name = name
        self.isdir = isdir
    
    
    
    

cwd = os.getcwd()
dirs = os.listdir()

def sort_dirs(all_items):
    new_list = []
    dirs = []
    files = []
    for item in all_items:
        if item.isdir:
            dirs.append(item)
        else:
            files.append(item)
    sorted(dirs, key=attrgetter('name'))
    sorted(files, key=attrgetter('name'))
    
    for item in dirs:
        new_list.append(item) 
    for item in files:
        new_list.append(item)
 
    return new_list
        

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"
    

def get_info():
    all_items = []
    for dir in dirs:
        permissions = oct(os.stat(dir).st_mode)[-3:]
        modtime = dt.datetime.fromtimestamp(os.path.getctime(dir)).strftime("%d %m %Y")
        isdir = None
        if not os.path.isdir(dir): 
            size = os.path.getsize(dir)
            isdir = False
        else:
            size = ''
            isdir = True
        

        all_items.append(Item(permissions, modtime, size, dir, isdir))

    new_list = sort_dirs(all_items)
    return new_list



######## RUN ##########
print()
print('-  ' + cwd)
print('\n')
print('\t Permissions \t Modified \t Size \t Name')
print('\t ----------- \t -------- \t ---- \t ----')
for item in get_info():
    print('\t\t' + str(item.permissions) + '\t' + str(item.modtime) + '\t' + str(item.size) + '\t' + item.name)
print()


