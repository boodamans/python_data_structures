def frequency(lst, search_term):
    result = 0
    for term in lst:
        if term == search_term:
            result = result + 1
    return result
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """