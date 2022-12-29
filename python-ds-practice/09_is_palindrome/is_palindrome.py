def is_palindrome(phrase):
    no_spaces = phrase.replace(' ','')
    flipped = no_spaces[::-1]
    upper = flipped.upper()
    return upper == upper[::-1]

    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
