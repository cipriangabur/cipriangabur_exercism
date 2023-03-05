"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers lasagna has.
    :return: int - preparation time in minutes.

    Function that takes the number of layers the lasagna has as
    an argument and returns how many minutes the layer still needs to bake
    based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers lasagna has.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time in minutes

    Function that takes the number of layers the lasagna has and elapsed baking time as
    arguments and returns how many minutes the lasagna needs to bake
    based on the `PREPARATION_TIME` and 'EXPECTED_BAKE_TIME'.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
