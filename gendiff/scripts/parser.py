import os
import json
from collections import ChainMap

def json_reader(file_name):
    CURRENT_DIR = os.getcwd()
    return {str(k): str(v) for k,v in json.load(open(file_name)).items()}

def check_difference(key, dict_1, dict_2):
    if key not in dict_2:
        return f"- {key}: {dict_1[key]}\n"
    elif key not in dict_1:
        return f"+ {key}: {dict_2[key]}\n"
    elif dict_1[key] != dict_2[key]:
        return f"- {key}: {dict_1[key]}\n+ {key}: {dict_2[key]}\n"
    else:
        return f"  {key}: {dict_1[key]}\n"

def generate_diff(first_file, second_file):
    file_1 = json_reader(first_file)
    file_2 = json_reader(second_file)
    all_keys = ChainMap(file_1, file_2).keys()
    result = '{\n'
    for key in sorted(all_keys):
        result += check_difference(key, file_1, file_2)
    result += '}'
    return result

def print_diff(difference):
    
    print('{', difference, '}')