import argparse

def args_parser():
    parser = argparse.ArgumentParser(prog="gendiff",
                                     usage="%(prog)s [-h] [-f FORMAT] fist_file, second_file",
                                     description= "Compares two configuration files and shows a difference.",
                                     )
    
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    return args.first_file, args.second_file