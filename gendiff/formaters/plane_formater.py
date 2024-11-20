import os
def plane(tree, path=''):
    result = []    
    for key, value in tree.items():        
        if not isinstance(value, dict):
            return ''
        if value.get("type", None) == "leaf":            
            result.append(plane_leaf_formater(key, value, os.path.join(path, key)))
                
        elif value.get("type", None) == "branch":
            
            result.extend(plane(value["children"], os.path.join(path, key)))
        
    return ''.join(result)

def plane_leaf_formater(key, leaf, path):
    path = path.replace('\\', '.')
    if leaf["status"] == "untouched":
        return ''
    elif leaf["status"] == "updated":        
        return f"Property {path} was updated. From '{complex_formater(leaf['old_value'])}' to '{complex_formater(leaf['new_value'])}'\n"
    elif leaf["status"] == "deleted":        
        return f"Property {path} was removed\n"
    elif leaf["status"] == "inserted":                
        return f"Property {path} was  added with value: {complex_formater(leaf['new_value'])}\n"
    
    

def complex_formater(value):
    if not isinstance(value, dict):
        return value
    return "[complex value]"