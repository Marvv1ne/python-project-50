import pytest
import os
from gendiff.engine import generate_diff

data_3_json = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file3.json')
data_4_json = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file4.json')
data_3_yml = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file3.yml')
data_4_yml = os.path.join(os.getcwd(), 'tests', 'fixtures', 'file4.yml')

correct_stylish_data_3 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'stylish_result_3_4.txt')
correct_plane_data_3 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'plane_result_3_4.txt')
correct_json_data_3 = os.path.join(os.getcwd(), 'tests', 'fixtures', 'result_3_4.json')


@pytest.mark.parametrize("data_1, data_2, format, result",
                         [(data_3_json, data_4_json, "stylish", correct_stylish_data_3),
                          (data_3_yml, data_4_yml, "stylish", correct_stylish_data_3),
                          (data_3_json, data_4_json, "plain", correct_plane_data_3),
                          (data_3_yml, data_4_yml, "plain", correct_plane_data_3),
                          (data_3_yml, data_4_json, "stylish", correct_stylish_data_3),
                          (data_3_json, data_4_yml, "stylish", correct_stylish_data_3),
                          (data_3_yml, data_4_json, "plain", correct_plane_data_3),
                          (data_3_json, data_4_yml, "plain", correct_plane_data_3)])
def test_gendiff(data_1, data_2, format, result):
    correct_result = open(result).read()
    assert generate_diff(data_1, data_2, format) == correct_result
