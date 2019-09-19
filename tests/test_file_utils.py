#!/bin/python3

import pytest

from utils import file_utils as futils
from src import consts
from models.user import User



"""
test read_file_lines
"""
def test_none_args():
    with pytest.raises(Exception) as e:
        futils.read_file_lines(None)

def test_no_file():
    with pytest.raises(Exception) as e:
        futils.read_file_lines("/lorem/ipsum")

def test_working_file():
    file_lines = futils.read_file_lines(consts.INPUT_FILE_PATH)
    assert isinstance(file_lines, list), "not a list"
    for line in file_lines:
        assert isinstance(line, str), "lines are not strings"


"""
test read_users_from_lines
"""
def test_none_args():
    with pytest.raises(Exception) as e:
        futils.read_users_from_lines(None)

def test_tuple_args():
    with pytest.raises(Exception) as e:
        futils.read_users_from_lines(("one", "two", "three"))

def test_non_str_list_args():
    with pytest.raises(Exception) as e:
        futils.read_users_from_lines([True, 0, False])

def test_empty_list_args():
    with pytest.raises(Exception) as e:
        futils.read_users_from_lines([])

def test_wrong_json_format_arg():
    with pytest.raises(Exception) as e:
        futils.read_users_from_lines(["{\"name\" : \"Andrew\""])

def test_working():
    line = "{\"latitude\": \"52.986375\", \"user_id\": 12, \"name\": \"Christina McArdle\", \"longitude\": \"-6.043701\"}"
    users = futils.read_users_from_lines([line])
    assert isinstance(users, list), "not a list"
    for user in users:
        assert isinstance(user, User), "not a user"
