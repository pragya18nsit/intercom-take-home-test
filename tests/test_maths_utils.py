#!/bin/python3

import math
import pytest
from decimal import Decimal

from utils.maths_utils import get_dist_between_coords, check_lat_arg, check_long_arg


"""
test check_lat_arg
"""
def test_none_args():
	assert check_lat_arg(None) == False, "check_lat_arg fails with None arg"

def test_str_args():
	assert check_lat_arg("str") == False, "check_lat_arg fails with str arg"

def test_too_small():
	assert check_lat_arg(-90.1) == False, "check_lat_arg fails with too small arg"

def test_too_large():
	assert check_lat_arg(90.1) == False, "check_lat_arg fails with too large arg"

def test_valid_lat():
	assert check_lat_arg(0) == True, "check_lat_arg fails with valid arg"

def test_valid_lat_1():
	assert check_lat_arg(53.95763) == True, "check_lat_arg fails with valids arg"


"""
test check_long_arg
"""
def test_none_args():
	assert check_long_arg(None) == False, "check_long_arg fails with None arg"

def test_str_args():
	assert check_long_arg("str") == False, "check_long_arg fails with str arg"

def test_too_small():
	assert check_long_arg(-180.1) == False, "check_long_arg fails with too small arg"

def test_too_large():
	assert check_long_arg(180.1) == False, "check_long_arg fails with too large arg"

def test_valid_lat():
	assert check_long_arg(0) == True, "check_long_arg fails with valid arg"

def test_valid_lat_1():
	assert check_long_arg(53.95763) == True, "check_long_arg fails with valids arg"



"""
test get_dist_between_coords
"""
def test_zero_args():
	with pytest.raises(Exception) as e:
		get_dist_between_coords(0, 0, 0, 0)

def test_same_place():
	with pytest.raises(Exception) as e:
		get_dist_between_coords(50.0, 6.25, 50.0, 6.25)

def test_args_none():
    with pytest.raises(Exception) as e:
    	get_dist_between_coords(None, None, None, None)

def test_args_string():
    with pytest.raises(Exception) as e:
    	get_dist_between_coords("string", "string", "string", "string")

def test_args_list():
    with pytest.raises(Exception) as e:
    	get_dist_between_coords([0,0,0], [0,0,0], [0,0,0], [0,0,0])

def test_args_bool():
    with pytest.raises(Exception) as e:
	    assert get_dist_between_coords(True, False, True, False)

def test_args_tuple():
    with pytest.raises(Exception) as e:
    	get_dist_between_coords((0,0,0), (0,0,0), (0,0,0), (0,0,0))

def test_args_dict():
    with pytest.raises(Exception) as e:
    	get_dist_between_coords({'i':0,'j':1}, {'i':0,'j':1}, {'i':0,'j':1}, {'i':0,'j':1})

def test_working():
	# checked using online calculator and random coords
	assert math.isclose(get_dist_between_coords(40.7486, -6.4826, -50.4826, 12.5626), Decimal('10313'), rel_tol=0.5) == True
