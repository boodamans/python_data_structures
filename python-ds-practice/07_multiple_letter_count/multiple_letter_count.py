def multiple_letter_count(phrase):
    result = {}
    for char in phrase:
        result[char] = phrase.count(char)
    return result
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """