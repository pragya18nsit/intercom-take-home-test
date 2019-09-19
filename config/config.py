#!/bin/python3

import os

"""
contains variables that will change from dev/prod environments
read from env variables
"""

PRINT_MESSAGES        = False if os.environ.get('PROD') else True
