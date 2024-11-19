def stylish(tree, depth=1):
    result = []
    spc = '..'
    for key, value in tree.items():
        if not isinstance(value, dict):
            result.append(f"  {key}: {dict_formater(value, spc, depth)}")
        elif value.get("type", None) == "branch":
            result.append(f"{spc*depth}  {key}: {{\n")
            result.append(f"{stylish(value['children'], depth+2)}\n")
            result.append(f"{spc*depth}}}\n")
        elif value.get("type", None) == "leaf":
            result.append(f"{leaf_formater(key, value, spc, depth)}")
    return ''.join(result)


def leaf_formater(key, leaf, spc, depth):
    res = []
    if leaf["status"] == "untouched":        
        res.append(f"{spc*depth}  {key}: {dict_formater(leaf['old_value'], spc, depth+2)}\n")
    elif leaf["status"] == "updated":        
        res.append(f"{spc*depth}- {key}: {dict_formater(leaf['old_value'], spc, depth+2)}\n")
        res.append(f"{spc*depth}+ {key}: {dict_formater(leaf['new_value'], spc, depth+2)}\n")
    elif leaf["status"] == "deleted":        
        res.append(f"{spc*depth}- {key}: {dict_formater(leaf['old_value'], spc, depth+2)}\n")
    elif leaf["status"] == "inserted":                
        res.append(f"{spc*depth}+ {key}: {dict_formater(leaf['new_value'], spc, depth+2)}\n")
    
    return ''.join(res)
        

def dict_formater(data, spc, depth):
    if not isinstance(data, dict):
        return data
    res = ['{']
    for k, v in data.items():
        res.append(f"\n{spc*depth}  {k}: {dict_formater(v, spc, depth+2)}\n")
    res.append(f"{spc*(depth-1)}}}")
    return ''.join(res)
