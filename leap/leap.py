"""
leap.py

File that contains functions for leap year calculation
"""


def leap_year(year):
    """
    This function has the purpose of recognizing if a year is leap or not.

    :param year: Year value (integer)
    :return: Bool: True or False
    """
    return False if year % 400 else True if year % 100 else False if year % 4 else True
