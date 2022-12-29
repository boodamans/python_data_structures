def single_letter_count(word, letter):
    filter_word = word.upper()
    filter_letter = letter.upper()
    return filter_word.count(filter_letter)
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """