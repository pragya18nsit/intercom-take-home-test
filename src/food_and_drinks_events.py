#!/bin/python3

from decimal import Decimal
from typing import List
import numbers
import os

from models.user import User
from utils import maths_utils
from config.config import PRINT_MESSAGES


"""
Contains functions related to food and drinks events at Intercom
"""

def get_users_within_dist(users: List[User], threshold_dist: Decimal, lat: Decimal, long: Decimal) -> List[User]:
    """
    Extracts users within dist of lat, long coordinate

    Args:
        users (List[User]): list of users.
        threshold_dist (Decimal): threshold distance.
        lat (Decimal): latitude.
        long (Decimal): longitude.

    Returns:
        List[User] list of users within distance
    """

    # check lines is a list
    if not isinstance(users, list):
        if PRINT_MESSAGES: print("[ERROR] parameter is not a list")
        raise Exception("parameter is not a list")

    # no users provided
    if len(users) == 0:
        if PRINT_MESSAGES: print("[ERROR] no users provided")
        raise Exception("no users provided")

    # check threshold
    if not isinstance(threshold_dist, numbers.Number):
        if PRINT_MESSAGES: print("[ERROR] threshold is not valid")
        raise Exception("threshold is not valid")

    if threshold_dist <= 0 and threshold_dist > 40075: # circumference of earth
        if PRINT_MESSAGES: print("[ERROR] threshold distance is not valid")
        raise Exception("threshold distance is not valid")

    # check lat and long
    if not maths_utils.check_lat_arg(lat) or not maths_utils.check_long_arg(long):
        if PRINT_MESSAGES: print("[ERROR] latitidues and longitudes are not valid")
        raise Exception("latitidues are not valid")



    invited_users = []
    for user in users:
        # calculate distance, check it is within range and add to list of invited guests
        # may throw exxception
        dist = maths_utils.get_dist_between_coords(user.latitude, user.longitude, lat, long)

        if dist < threshold_dist:
            invited_users.append(user)


    # if there is no one in range, print message and exit
    if len(invited_users) == 0:
        if PRINT_MESSAGES: print("[ERROR] no users within distance")
        raise Exception("no users are within the distance")

    return invited_users






def write_guest_to_file(users: List[User], path: str) -> bool:
    """
    Attempts to write a list of guests to the output file

    Args:
        users (List[User]): list of invited users.
        path (str): path to the file to be written to.

    Returns:
        True: if completed
    """

    # check lines is a list
    if not isinstance(users, list):
        if PRINT_MESSAGES: print("[ERROR] parameter is not a list")
        raise Exception("paramter is not a list")

    # no lines in the file so print error message and return
    if len(users) == 0:
        if PRINT_MESSAGES: print("[ERROR] no users provided")
        raise Exception("no users provided")


    if os.path.isfile(path):

        try:
            #open file in write mode, write and close
            with open(path, 'w') as f:

                # only write name and user_id, cast user_id to str
                for user in users:
                    f.write(user.name + " " + str(user.user_id)+"\n")

                return True


        # can't open the file even if found: e.g. permissions
        except:
            if PRINT_MESSAGES: print("[ERROR] cannot open file")
            raise Exception("cannot open file")

    # fails because we can't find the file
    else:
        if PRINT_MESSAGES: print("[ERROR] cannot find file")
        raise Exception("cannot find file")
