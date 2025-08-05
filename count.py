# Probelm 4 4a. below. Prepearing for loops

def count(letter, string):
    '''takes a letter as input (a string with just one symbol in it) and returns the number of times that the given letter appears in the given string.'''
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

