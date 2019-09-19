#!/bin/python3

import math
import numbers
from decimal import Decimal
from config.config import PRINT_MESSAGES

from src import consts


def check_lat_arg(lat: Decimal) -> bool:
    """
    Checks whether a latitude argument is valid.

    Args:
        lat (Decimal): latitude to be checked.

    Returns:
        True: if valid.
        False: if not valid.
    """

    # check is a number
    if isinstance(lat, numbers.Number):

        # check is within bounds
        if lat >= -90 and lat <= 90:
            return True
        else:
            return False

    else:
        return False




def check_long_arg(long: Decimal) -> bool:
    """
    Checks whether a longitude argument is valid.

    Args:
        lat (Decimal): longitude to be checked.

    Returns:
        True: if valid.
        False: if not valid.
    """

    # check is a number
    if isinstance(long, numbers.Number):

        # check is within bounds
        if long >= -180 and long <= 180:
            return True
        else:
            return False

    else:
        return False




def get_dist_between_coords(lat1: Decimal, long1: Decimal, lat2: Decimal, long2: Decimal) -> Decimal:
    """
    Calculates distance between two coordinates using great-circle distance:
    https://en.wikipedia.org/wiki/Great-circle_distance

    Args:
        lat1 (Decimal): latitude of first coordinate.
        long1 (Decimal): longitude of first coordinate.
        lat2 (Decimal): latitude of second coordinate.
        long2 (Decimal): longitude of second coordinate.

    Returns:
        Decimal: returns distance in kms.
    """

    if not check_lat_arg(lat1) or not check_lat_arg(lat2):
        if PRINT_MESSAGES: print("[ERROR] latitidues are not valid")
        raise Exception("latitidues are not valid")

    if not check_long_arg(long1) or not check_long_arg(long2):
        if PRINT_MESSAGES: print("[ERROR] longitudes are not valid")
        raise Exception("longitudes are not valid")


    # check if same place
    if lat1 == lat2 and long1 == long2:
        if PRINT_MESSAGES: print("[ERROR] point 1 and 2 are the same place")
        raise Exception("point 1 and 2 are the same place")


    #convert params to radians
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)


    #compute
    diff_lat = long1 - long2
    central_angle = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(diff_lat))
    surface_distance = consts.EARTH_RADIUS * Decimal(central_angle)

    return surface_distance
