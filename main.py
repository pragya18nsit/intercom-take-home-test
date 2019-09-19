#!/bin/python3

# import our modules
from models.user import User
from utils import file_utils
from utils import maths_utils
from src import consts
from config.config import PRINT_MESSAGES
from src.food_and_drinks_events import get_users_within_dist, write_guest_to_file



def main():


    # attempt to read lines from input file
    try:
        file_lines = file_utils.read_file_lines(consts.INPUT_FILE_PATH)
    except Exception as e:
        if PRINT_MESSAGES: print("[FATAL ERROR] "+str(e))
        exit()


    # attempt to read users from the lines
    try:
        users = file_utils.read_users_from_lines(file_lines)
    except Exception as e:
        if PRINT_MESSAGES: print("[FATAL ERROR] "+str(e))
        exit()


    # attempt to get all users within distance
    try:
        invited_users = get_users_within_dist(users, consts.THRESHOLD_DISTANCE, consts.DUBLIN_LATTITUDE, consts.DUBLIN_LONGITUDE)
    except Exception as e:
        if PRINT_MESSAGES: print("[FATAL ERROR] "+str(e))
        exit()


    # sort users by ascending id
    invited_users = sorted(invited_users, key = lambda i: i.user_id)


    # write the guests to the output file
    try:
        write_guest_to_file(invited_users, consts.OUTPUT_FILE_PATH)
        if PRINT_MESSAGES: print("[SUCCESS] have written invited guests to "+consts.OUTPUT_FILE_PATH)

    except Exception as e:
        if PRINT_MESSAGES: print("[FATAL ERROR] "+str(e))
        exit()



if __name__ == '__main__':
    main()
