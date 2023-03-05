import string
lwr_case_alphabet = list(string.ascii_lowercase)


def is_pangram(sentence):
    """
    This method has the purpose of checking if a text (given by sentence) is a pangram.
    A pangram (Greek: παν γράμμα, pan gramma, "every letter") is a sentence using every letter of the
    lwr_case_alphabet at least once.
    The best known English pangram is:

    The quick brown fox jumps over the lazy dog.

    :param sentence: The sentence that needs to be checked for pangram
    :return: True if the sentence is a pangram, False otherwise
    """
    if len(sentence):
        return all(char in sentence.lower() for char in lwr_case_alphabet)
    return False
