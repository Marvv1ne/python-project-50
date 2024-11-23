from gendiff.cli import args_parser
from gendiff.engine import generate_diff


def main():
    first_file, second_file, format = args_parser()
    print(generate_diff(first_file, second_file, format))


if __name__ == "__main__":
    main()
