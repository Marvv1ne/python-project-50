from ..tree import get_old_value, get_new_value, get_children
from ..parser import converter


def to_string(tree, depth=1):
    result = []
    spc = '  '
    for key, value in tree.items():
        if not isinstance(value, dict):
            result.append(f"  {key}: {dict_formater(value, spc, depth)}")
        elif value.get("type", None) == "branch":
            result.append(f"{spc * depth}  {key}: {{\n")
            result.append(f"{to_string(get_children(value), depth + 2)}")
            result.append(f"{spc * (depth + 1)}}}\n")
        elif value.get("type", None) == "leaf":
            result.append(f"{leaf_formater(key, value, spc, depth)}")
    return ''.join(result)


def leaf_formater(key, leaf, spc, depth):
    res = []
    if leaf["status"] == "untouched":
        str_key = f"{spc * depth}  {key}: "
        str_value = f"{dict_formater(get_old_value(leaf), spc, depth + 2)}\n"
        res.append(str_key + str_value)
    elif leaf["status"] == "updated":
        str_key = f"{spc * depth}- {key}: "
        str_value = f"{dict_formater(get_old_value(leaf), spc, depth + 2)}\n"
        res.append(str_key + str_value)
        str_key = f"{spc * depth}+ {key}: "
        str_value = f"{dict_formater(get_new_value(leaf), spc, depth + 2)}\n"
        res.append(str_key + str_value)
    elif leaf["status"] == "deleted":
        str_key = f"{spc * depth}- {key}: "
        str_value = f"{dict_formater(get_old_value(leaf), spc, depth + 2)}\n"
        res.append(str_key + str_value)
    elif leaf["status"] == "inserted":
        str_key = f"{spc * depth}+ {key}: "
        str_value = f"{dict_formater(get_new_value(leaf), spc, depth + 2)}\n"
        res.append(str_key + str_value)
    return ''.join(res)


def dict_formater(data, spc, depth):
    if not isinstance(data, dict):
        return converter(data)
    res = ['{']
    for k, v in data.items():
        str_key = f"\n{spc * depth}  {k}: "
        str_value = f"{dict_formater(v, spc, depth + 2)}"
        res.append(str_key + str_value)
    res.append(f"\n{spc * (depth - 1)}}}")
    return ''.join(res)


def stylish_formater(tree):
    return f"{{\n{to_string(tree)}}}"
