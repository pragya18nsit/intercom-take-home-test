#!/bin/python3

import os
import json
from typing import List

# import our modules
from config.config import PRINT_MESSAGES
from models.user import User

"""
contains functions related to file handling
"""


def read_file_lines(path: str) -> List[str]:
    """
    Utility function to open a file and return a list of lines

    Args:
        path (str): path to the file to be opened.

    Returns:
        List[str]: list of lines (str) in the file.
    """

    if os.path.isfile(path):

        try:
            #open file in read mode, read, and then close
            f = open(path, 'r')
            line_list = f.readlines()
            f.close()
            return line_list

        # can't open the file even if found: e.g. permissions
        except:
            if PRINT_MESSAGES: print("[ERROR] cannot open file")
            raise Exception("cannot open file")

    # fails because we can't find the file
    else:
        if PRINT_MESSAGES: print("[ERROR] cannot find file")
        raise Exception("cannot find file")




def read_users_from_lines(lines: List[str]) -> List[User]:
    """
    Utility function to read users from lines

    Args:
        lines (List[str]): lines in a file

    Returns:
        List[User]: list of lines (str) in the file.
    """

    users = []

    # check lines is a list
    if not isinstance(lines, list):
        if PRINT_MESSAGES: print("[ERROR] parameter is not a list")
        raise Exception("paramter is not a list")

    # no lines in the file so print error message and return
    if len(lines) == 0:
        if PRINT_MESSAGES: print("[ERROR] no lines in file")
        raise Exception("file is empty")


    for line in lines:

        # attempt to convert line to dict
        # will also catch if line is not a string
        try:
            data = json.loads(line.strip())

        # if incorrectly formatted, then print error message and exit
        except:
            if PRINT_MESSAGES: print("[ERROR] incorrectly formatted file")
            raise Exception("incorrectly formatted file")

        # construct user object and add to list
        users.append(User(data['name'], data['user_id'], data['latitude'], data['longitude']))

    return users
