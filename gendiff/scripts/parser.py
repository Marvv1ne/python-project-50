import os
import json
import yaml

from collections import ChainMap

def converter(value):
    json_bools = {None: 'null', True: 'true', False: 'false'}
    if type(value) == dict:
        return value
    elif type(value) == str:
        return value
    elif type(value) == bool:
        return json_bools[value]
    elif value == None:
        return json_bools[value]
    elif type(value) == int:
        return str(value)
        
        

def get_suffix(file_name):
    return file_name.split('.')[-1]

def file_reader(file_name):
    current_dir = os.path.join(os.getcwd(), file_name)
    suffix = get_suffix(file_name)
    match suffix:
        case 'json':
            return json.load(open(current_dir))
        case 'yaml':
            return yaml.safe_load(open(current_dir))
        case 'yml':
            return yaml.safe_load(open(current_dir))
