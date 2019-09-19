#!/bin/python3

from decimal import Decimal

class User:

    """
    Class to represent a user on the Intercom application.
    """

    def __init__(self, name: str, user_id: int, latitude: Decimal, longitude: Decimal):
        """
        Constructs user

        Args:
            name (str): full name of user.
            user_id (int): id of user.
            latitude (Decimal): latitude of user.
            longitude (Decimal): longitude of user.
        """

        # will attempt to cast here just to be safe
        self.name = str(name)
        self.user_id = int(user_id)
        self.latitude = Decimal(latitude)
        self.longitude = Decimal(longitude)
