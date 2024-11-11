from pprint import pprint
from .cli import args_parser
from .parser import generate_diff

def main():
    file1, file2 = args_parser()
    pprint(generate_diff(file1, file2))
    

if __name__ == "__main__":
    main()  
