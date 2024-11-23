import os
import json
import yaml


def converter(value):
    json_bools = {None: 'null', True: 'true', False: 'false'}
    if isinstance(value, dict):
        return value
    elif isinstance(value, str):
        return value
    elif isinstance(value, bool):
        return json_bools[value]
    elif value is None:
        return json_bools[value]
    elif isinstance(value, int):
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
