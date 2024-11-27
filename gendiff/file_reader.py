import os


def get_data_format(file_name):
    return file_name.split('.')[-1]


def file_reader(file_name):
    current_dir = os.path.join(os.getcwd(), file_name)
    with open(current_dir) as file:
        data = file.read()
    return data
