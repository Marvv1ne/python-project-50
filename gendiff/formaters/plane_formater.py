import os
from ..scripts.parser import converter
from ..scripts.tree import get_children, get_new_value, get_old_value
def plane_formater(tree, path=''):
    result = []
    
    for key, value in tree.items():
        
        if not isinstance(value, dict):
            return ''
        if value.get("type", None) == "leaf":            
            result.append(plane_leaf_formater(key, value, os.path.join(path, key)))                
        elif value.get("type", None) == "branch":            
            result.extend(plane_formater(get_children(value), os.path.join(path, key)))        
    return ''.join(result)

def plane_leaf_formater(key, leaf, path):
    path = path.replace('\\', '.')
    res = ''
    if leaf["status"] == "untouched":
        return ''
    elif leaf["status"] == "updated":
        res = f"Property {path} was updated. "
        res += f"From '{complex_formater(get_old_value(leaf))}' to "
        res += f"'{complex_formater(get_new_value(leaf))}'\n"        
    elif leaf["status"] == "deleted":       
        res += f"Property {path} was removed\n"
    elif leaf["status"] == "inserted":                
        res += f"Property {path} was added with value: "
        res += f"{complex_formater(get_new_value(leaf))}\n"
    return res
    

def complex_formater(value):
    if not isinstance(value, dict):
        return converter(value)
    return "[complex value]"