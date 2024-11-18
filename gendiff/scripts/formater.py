def stylish(tree, depth=1):
    result = []
    space = '..'
    for key, value in tree.items():
        if value.get("status", None) == "updated":
            result.extend([f"{space*depth}- {key}: {value["old_value"]}\n",
                               f"{space*depth}+ {key}: {value["old_value"]}\n"])
        elif value.get("status", None) == "deleted":
            result.append(f"{space*depth}- {key}: {value["old_value"]}\n")
        elif value.get("status", None) == "inserted":
            result.append(f"{space*depth}+ {key}: {value["new_value"]}\n")
        elif value.get("status", None) == "untouched":
            result.append(f"{space*depth}  {key}: {value["old_value"]}\n")
        else:
            result.append(f"{space*depth}  {key}: \n{space*depth}{stylish(value, depth+2)}")
    return ''.join(result)
        