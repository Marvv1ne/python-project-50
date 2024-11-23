import os
from ..parser import converter
from ..tree import get_children, get_new_value, get_old_value


def plane_formater(tree, path=''):
    result = []
    for key, value in tree.items():
        if not isinstance(value, dict):
            return ''
        if value.get("type", None) == "leaf":
            result.append(plane_leaf_formater(value,
                                              os.path.join(path, key)))
        elif value.get("type", None) == "branch":
            result.extend(plane_formater(get_children(value),
                                         os.path.join(path, key)))
    return ''.join(result)


def plane_leaf_formater(leaf, path):
    path = path.replace('/', '.')
    res = ''
    if leaf["status"] == "untouched":
        return ''
    elif leaf["status"] == "updated":
        res = f"Property '{path}' was updated. "
        res += f"From {type_formater(get_old_value(leaf))} to "
        res += f"{type_formater(get_new_value(leaf))}\n"
    elif leaf["status"] == "deleted":
        res += f"Property '{path}' was removed\n"
    elif leaf["status"] == "inserted":
        res += f"Property '{path}' was added with value: "
        res += f"{type_formater(get_new_value(leaf))}\n"
    return res


def type_formater(value):
    value = converter(value)
    if isinstance(value, dict):
        return "[complex value]"
    elif value in ("null", "true", "false"):
        return value
    elif isinstance(value, str):
        return f"'{value}'"
