def is_anagram(word1, word2):
    """
    Returns True if the two words are anagrams of each other, without being the same words.
    False otherwise.
    """
    # convert the words to lowercase and remove spaces
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')

    # check if the sorted letters of the two words match
    return False if word1 == word2 else sorted(word1) == sorted(word2)


def find_anagrams(word, candidates):
    """
    Returns a list of all the words in candidates that are anagrams of word.
    """
    return [candidate for candidate in candidates if is_anagram(word, candidate)]

