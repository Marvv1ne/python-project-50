def stylish(tree, depth=1):
    result = []
    space = '..'
    for key, value in tree.items():
        if value.get("status", None) == "updated":
            result.extend([f"{space*depth}- {key}: {dict_formater(value["old_value"], space, depth+2)}\n",
                               f"{space*depth}+ {key}: {dict_formater(value["old_value"], space, depth+2)}\n"])
        elif value.get("status", None) == "deleted":
            result.append(f"{space*depth}- {key}: {dict_formater(value["old_value"], space, depth+2)}\n")
        elif value.get("status", None) == "inserted":
            result.append(f"{space*depth}+ {key}: {dict_formater(value["new_value"], space, depth+2)}\n")
        elif value.get("status", None) == "untouched":
            result.append(f"{space*depth}  {key}: {dict_formater(value["old_value"], space, depth+2)}\n")
        else:
            result.append(f"{space*depth}  {key}: \n{stylish(value, depth+2)}")
    return ''.join(result)


def dict_formater(tree, space, depth):
    result = []
    if not isinstance(tree, dict):
        return tree
    for k, v in tree.items():
        result.append(f"\n{space*(depth)}  {k}: {dict_formater(v, space, depth+2)}")
    return ''.join(result)        