#!/bin/python3

from decimal import Decimal

EARTH_RADIUS        = Decimal('6371') # km
THRESHOLD_DISTANCE  = Decimal('100.0') # km
DUBLIN_LATTITUDE    = Decimal('53.339428')
DUBLIN_LONGITUDE    = Decimal('-6.257664')
INPUT_FILE_PATH     = './res/customers.txt' # relative to main.py
OUTPUT_FILE_PATH    = './res/output.txt' # relative to main.py
