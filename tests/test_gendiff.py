import pytest
import os
from gendiff.scripts.parser import generate_diff

data_1 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file1.json')
data_2 = os.path.join(os.path.dirname(__file__), 'fixtures', 'file2.json')

def test_gendiff():
    correct = """{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}"""
    assert generate_diff(data_1, data_2) == correct