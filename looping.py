# Problem 1a.

from typing import List


def countLength(dnaList: List[str], length: int) -> int:
    '''Takes a list of DNA strings called DNAlist and a positive integer length 
    as input and returns the number of strings in the list that have the specified length.
    
    Args:
        dnaList: List of DNA sequence strings
        length: Target length to count
        
    Returns:
        Number of strings with the specified length
    '''
    # Optimized: use sum with generator expression (more Pythonic)
    return sum(1 for seq in dnaList if len(seq) == length)


# Problem 1b.

def getLength(DNAlist: List[str], length: int) -> List[str]:
    '''Takes a list of DNA strings called DNAlist and a positive integer length 
    as input and returns a list of the strings of that length.
    
    Args:
        DNAlist: List of DNA sequence strings
        length: Target length to filter
        
    Returns:
        List of strings matching the specified length
    '''
    # Optimized: use list comprehension (faster and more Pythonic)
    return [dna_string for dna_string in DNAlist if len(dna_string) == length]


# Problem 1c.

def factorial(n: int) -> int:
    '''Takes a positive integer n as input and returns n!.
    
    Args:
        n: Positive integer
        
    Returns:
        Factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
    '''
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    
    counter = 1
    for i in range(2, n + 1):  # Start from 2 (slight optimization)
        counter *= i
    return counter


# Test code (run only when script is executed directly)
if __name__ == '__main__':
    # Test countLength
    dnaList = ['AAA', 'ACGAC', 'CG', 'TCA']
    assert countLength(dnaList, 4) == 0
    assert countLength(dnaList, 3) == 2
    
    # Test getLength
    assert getLength(["ATA", "ATCG", "TTT", "A"], 3) == ['ATA', 'TTT']
    
    # Test factorial
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(4) == 24
    
    print("All tests passed!")
