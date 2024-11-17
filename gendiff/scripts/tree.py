from collections import ChainMap
from .parser import converter

def make_updated_leaf(key, old_value, new_value):
    return {f"- {key}": converter(old_value), f"+ {key}": converter(new_value)}

def make_deleted_leaf(key, value):
    return {f"- {key}": converter(value)}

def make_inserted_leaf(key, value):
    return {f"+ {key}": converter(value)}

def make_untouched_leaf(key, value):
    return {f"  {key}": converter(value)}

def make_branch(key, make_leaf):
    return {f"{key}": make_leaf}

def check_leaf(key, old_dict, new_dict):
    diff_old_new = old_dict.keys() - new_dict.keys()
    diff_new_old = new_dict.keys() - old_dict.keys()
    intersection = old_dict.keys() & new_dict.keys()
    if key in diff_old_new:
        value = old_dict[key]
        return make_deleted_leaf(key, value)
    elif key in diff_new_old:
        value = new_dict[key]
        return make_inserted_leaf(key, value)
    elif key in intersection:
        old_value = old_dict[key]
        new_value = new_dict[key]
        return make_updated_leaf(key, old_value, new_value) if old_value != new_value else make_untouched_leaf(key, old_value)
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
            #print(old_dict, new_dict)
            tree.update(check_leaf(key, old_dict, new_dict))
        else:
            old_value = old_dict.get(key, dict())
            new_value = new_dict.get(key, dict())
            tree.update({key: make_tree(old_value, new_value)})
    return tree
