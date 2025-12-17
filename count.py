# Problem 4 4a. below. Preparing for loops

from typing import Union


def count(letter: str, string: str) -> int:
    '''takes a letter as input (a string with just one symbol in it) and returns the number of times that the given letter appears in the given string.
    
    Args:
        letter: A single character to count
        string: The string to search in
        
    Returns:
        int: Number of occurrences of letter in string
        
    Raises:
        ValueError: If letter is not a single character
        TypeError: If inputs are not strings
    '''
    # Input validation
    if not isinstance(letter, str) or not isinstance(string, str):
        raise TypeError("Both letter and string must be strings")
    if len(letter) != 1:
        raise ValueError("letter must be a single character")
    
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

