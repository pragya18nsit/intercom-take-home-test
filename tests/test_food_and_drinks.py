#!/bin/python3


import pytest

from models.user import User
from src.food_and_drinks_events import get_users_within_dist, write_guest_to_file


"""
test get_users_within_dist
"""
def test_none_args():
    with pytest.raises(Exception) as e:
        get_users_within_dist(None, None, None, None)

def test_invalid_lat_longs():
    with pytest.raises(Exception) as e:
        get_users_within_dist(None, None, -90.1, 180.1)

def test_invalid_threshold_dist():
    with pytest.raises(Exception) as e:
        get_users_within_dist([User()], -10, 60.34, 54.0)


"""
test write_guest_to_file
"""
def test_none_args():
    with pytest.raises(Exception) as e:
        write_guest_to_file(None, None)

def test_no_users():
    with pytest.raises(Exception) as e:
        write_guest_to_file([], None)

def test_no_file():
    with pytest.raises(Exception) as e:
        write_guest_to_file(["mock"], "/lorem/ipsum")
