color_mapping = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9}


def color_code(color):
    """
    This function has the purpose of returning the resistance of a specific resistor color.

    :param color: The color of the resistor (check colors dictionary for additional context)
    :return: Numerical value of resistance for a specific resistor color given by param color.
    """
    return color_mapping.get(color.lower()) if color in list(color_mapping.keys()) else None


def colors():
    """
    This function has the purpose of returning the color names stored in color_mapping.

    :return: A list of color names stored in color_mapping.
    """
    return [color_name for color_name in color_mapping.keys()]
