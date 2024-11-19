from collections import ChainMap
from .parser import converter

def mkbranch(value):
    return {"children": value, "type": "branch"}

def mkleaf(old_value=None, new_value=None, status=None):
    return {"old_value": old_value,
            "new_value": new_value,
            "status": status,
            "type": "leaf"}

def make_updated_leaf(old_value, new_value):
    return mkleaf(old_value=old_value, new_value=new_value, status="updated")

def make_deleted_leaf(old_value):
    return mkleaf(old_value=old_value, status="deleted")

def make_inserted_leaf(new_value):
    return mkleaf(new_value=new_value, status="inserted")

def make_untouched_leaf(value):
    return mkleaf(old_value=value, new_value=value, status="untouched")


def check_leaf(key, old_dict, new_dict):
    diff_old_new = old_dict.keys() - new_dict.keys()
    diff_new_old = new_dict.keys() - old_dict.keys()
    intersection = old_dict.keys() & new_dict.keys()
    if key in diff_old_new:
        old_value = old_dict[key]
        return {key: make_deleted_leaf(old_value)}
    elif key in diff_new_old:
        new_value = new_dict[key]
        return {key: make_inserted_leaf(new_value)}
    elif key in intersection:
        old_value = old_dict[key]
        new_value = new_dict[key]
        return {key: make_updated_leaf(old_value, new_value)} if old_value != new_value else {key: make_untouched_leaf(old_value)}
    else:
        return "I dont know what to do sir!"

def is_branch(key, old_dict, new_dict):
    if type(old_dict) == str or type(new_dict) == str:
        return False
    old_value = old_dict.get(key, None)
    new_value = new_dict.get(key, None)
    return isinstance(old_value, dict) and isinstance(new_value, dict)

def make_tree(old_dict, new_dict):
    tree = {}
    all_keys = sorted(ChainMap(old_dict, new_dict))
    
    for key in all_keys:
        if not is_branch(key, old_dict, new_dict):
            tree.update(check_leaf(key, old_dict, new_dict))
        else:
            old_value = old_dict.get(key, dict())
            new_value = new_dict.get(key, dict())
            tree.update({key: mkbranch(make_tree(old_value, new_value))})
    return tree