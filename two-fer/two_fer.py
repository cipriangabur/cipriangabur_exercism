"""
two_fer.py module
"""


def two_fer(name="you"):
    """
    This function has the purpose of returning a text containing "One for x, one for me.", x being either a name,
    either string "you".

    :param name: The name that needs to be used in the ending text.
    :return: Text containing "One for {name}, one for me."
    """
    return f"One for {name}, one for me."
