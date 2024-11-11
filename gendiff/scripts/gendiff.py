from pprint import pprint
from .cli import args_parser
from .parser import generate_diff, print_diff

def main():
    file1, file2 = args_parser()
    difference = generate_diff(file1, file2)
    print_diff(difference)
    

if __name__ == "__main__":
    main()  
