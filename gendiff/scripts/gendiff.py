import argparse
def gendiff():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="gendiff",
                                     usage="%(prog)s [-h] fist_file, second_file",
                                     description= "Compares two configuration files and shows a difference.",
                                     )
    
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
