from .tree import make_tree
from .parser import file_reader
from .formaters.stylish_formater import stylish_formater
from .formaters.plane_formater import plane_formater
from .formaters.json_formater import json_formater


def generate_diff(first_file_name, second_file_name, format="stylish"):
    old_dict = file_reader(first_file_name)
    new_dict = file_reader(second_file_name)
    tree = make_tree(old_dict, new_dict)
    match format:
        case "stylish":
            return stylish_formater(tree)
        case "plane":
            return plane_formater(tree).rstrip()
        case "json":
            return json_formater(tree)
