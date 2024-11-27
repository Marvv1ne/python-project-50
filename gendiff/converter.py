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
        return value
