from pprint import pprint
from .cli import args_parser
from .tree import make_tree
from .parser import file_reader
from pprint import pprint
from ..formaters.stylish_formater import stylish
from ..formaters.plane_formater import plane


def generate_diff(first_file_name, second_file_name, format):
    old_dict = file_reader(first_file_name)
    new_dict = file_reader(second_file_name)
    tree = make_tree(old_dict, new_dict)
    match format:
        case "stylish":
            return stylish(tree)
        case "plane":
            return plane(tree)
    

def main():
    first_file, second_file, format = args_parser()
    print(generate_diff(first_file, second_file, format))   
    

if __name__ == "__main__":
    main()
