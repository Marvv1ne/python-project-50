from .tree import make_tree
from .file_reader import file_reader, get_data_format
from .parser import parser
from .formaters.stylish_formater import stylish_formater
from .formaters.plane_formater import plane_formater
from .formaters.json_formater import json_formater


def generate_diff(first_file_name, second_file_name, format="stylish"):
    old_data = file_reader(first_file_name)
    new_data = file_reader(second_file_name)
    old_data_format = get_data_format(first_file_name)
    new_data_format = get_data_format(second_file_name)
    old_dict = parser(old_data, old_data_format)
    new_dict = parser(new_data, new_data_format)
    tree = make_tree(old_dict, new_dict)
    match format:
        case "stylish":
            return stylish_formater(tree)
        case "plain":
            return plane_formater(tree).rstrip()
        case "json":
            return json_formater(tree)
