import json
import yaml


def parser(data, data_format):
    match data_format:
        case 'json':
            return json.loads(data)
        case 'yaml':
            return yaml.safe_load(data)
        case 'yml':
            return yaml.safe_load(data)
        case _:
            raise ValueError("Invalid data format")
