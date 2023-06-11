def is_isogram(string):
    """
    Function used to check if a specific string given by parameter is isogram or not.

    :param string: The string that needs to be checked for isogram check.
    :return bool: Returns True if the string is isogram, False otherwise
    """
    without_special_chars = "".join(char.lower() for char in string if char.isalnum())
    return len(without_special_chars) == len(set(without_special_chars))
