import os
import json

def file_reader(file_name):
    CURRENT_DIR = os.getcwd()
    return json.load(open(f'{CURRENT_DIR}/{file_name}'))
    
def generate_diff(first_file, second_file):
    file_1 = file_reader(first_file)
    file_2 = file_reader(second_file)
    return file_1, file_2
    