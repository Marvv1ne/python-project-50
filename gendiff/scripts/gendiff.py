from pprint import pprint
from .cli import args_parser
from .tree import make_tree
from .parser import file_reader
from pprint import pprint
from .formater import stylish

def generate_diff(first_file_name, second_file_name):
    old_dict = file_reader(first_file_name)
    new_dict = file_reader(second_file_name)
    return make_tree(old_dict, new_dict)

def main():
    first_file, second_file = args_parser()
    diff = generate_diff(first_file, second_file)
    print(stylish(diff))   
    

if __name__ == "__main__":
    main()
