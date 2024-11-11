import os
import json
from collections import ChainMap

def json_reader(file_name):
    CURRENT_DIR = os.getcwd()
    return json.load(open(f'{CURRENT_DIR}/{file_name}'))

def generate_diff(first_file, second_file):
    file_1 = json_reader(first_file)
    file_2 = json_reader(second_file)
    file_d = ChainMap(file_1, file_2)
    result = '\n'
    for key in sorted(file_d.keys()):
        if key not in file_2:
            result += f"- {key}: {file_1[key]}\n"
        elif key not in file_1:
            result += f"+ {key}: {file_2[key]}\n"
        elif file_1[key] != file_2[key]:
            result += f"- {key}: {file_1[key]}\n"
            result += f"- {key}: {file_2[key]}\n"
        else:
            result += f"  {key}: {file_1[key]}\n"
    return result

def print_diff(difference):
    
    print('{', difference, '}')