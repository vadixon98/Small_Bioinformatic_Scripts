# Illustrative code for CFB, Chapter 2

# Topics covered previously in course:
# - Installing Python & IDLE (on PC & Mac)
# - Basic Math in Python
# - Variables & Assignment
# - Introduction to Strings
# - Introduction to Lists
# - Boolean Expressions
# - Writing Simple Functions
# - Decisions (with if, elif, and else)
# - Definite Loops ("for loops")

# In Chapter 2 we'll cover:
# - For Loops in more detail
# - For Looping over Lists
# - Using For Loops to find GC content
# - Using For Loops to locate motifs
# - Functions Calling Other Functions
# - For Looping over Lists of Strings

# I've written a single program that contains
# several functions to illustrate the coding
# strategies mentioned above.

# Here's a list that we will use to test this program:
# my_list = ['gtaccgt', 'gtaccca', 'ttacatg', 'acgggac']

from typing import List, Tuple, Optional

# Constants
GC_RICH_THRESHOLD = 55.0  # Percentage threshold for GC-rich sequences
START_CODON = 'atg'


def t_finder(some_list: List[str]) -> int:
    ''' finds number of strings with >= 2 ts (case-insensitive)'''
    
    counter = 0
    
    for seq in some_list:
        num_ts = seq.lower().count('t')
        if num_ts >= 2:
            counter = counter + 1

    return counter


def GC_maker(some_list: List[str]) -> List[int]:
    '''finds GC content of strings in a list (case-insensitive)'''  

    GC_results = []

    for seq in some_list:
        seq_lower = seq.lower()
        num_cs = seq_lower.count('c')
        num_gs = seq_lower.count('g')
        GC_count = num_cs + num_gs
        GC_results.append(GC_count)

    return GC_results


def GC_rich(some_list: List[str], threshold: float = GC_RICH_THRESHOLD) -> List[float]:
    '''Finds GC rich strings in a list (case-insensitive, threshold >= 55% by default).
    
    Args:
        some_list: List of DNA sequence strings
        threshold: GC percentage threshold (default: 55.0)
        
    Returns:
        List of GC percentages for sequences meeting the threshold
    '''
    GC_much = []

    for seq in some_list:
        if len(seq) == 0:  # Handle empty strings
            continue
        seq_lower = seq.lower()
        num_cs = seq_lower.count('c')
        num_gs = seq_lower.count('g')
        GC_count = num_cs + num_gs
        GC_perc = 100 * (GC_count / len(seq))
        if GC_perc >= threshold:
            GC_much.append(round(GC_perc, 2))

    return GC_much


def string_start(seq: str) -> Tuple[bool, Optional[int]]:
    '''Checks string for potential start codon (case-insensitive).
    
    Args:
        seq: DNA sequence string to search
        
    Returns:
        Tuple of (found: bool, location: Optional[int])
            found: True if start codon found, False otherwise
            location: Index of start codon if found, None otherwise
    '''
    # Stop 2 positions before end to avoid index out of bounds
    for index in range(len(seq) - 2):
        if seq[index:index+3].lower() == START_CODON:
            return (True, index)  # Return immediately when found

    return (False, None)  # Return False and None if not found
            

def list_start(some_list: List[str]) -> List[Tuple[bool, Optional[int]]]:
    '''Finds strings in list that may have a start codon.
    
    Args:
        some_list: List of DNA sequence strings
        
    Returns:
        List of tuples (found: bool, location: Optional[int]) for each sequence
    '''
    # Optimized: use list comprehension
    return [string_start(seq) for seq in some_list]


def seq_analyzer(some_list: List[str]) -> None:
    '''uses above defined functions to evaluate seqs in list'''
    
    print("")
    print("The number of sequences in this list that have")
    print("at least 2 t's is:", t_finder(some_list))
    print("")
    
    print("The sequences differ in the number of Gs and Cs they have.")
    print("The number of Gs and Cs in each seq is:")
    print("")
    print(GC_maker(some_list))
    print("")

    print("Some of the sequences are GC rich. The GC % of these")
    print("sequences is:")
    print("")
    print(GC_rich(some_list))
    print("")
          
    print("Some sequences have potential start codons.")
    print("For each seq here are: (1) whether a possible start is")
    print("present, and (2) if so, its location in seq:")
    print("")
    start_results = list_start(some_list)
    for i, (found, location) in enumerate(start_results):
        if found:
            print(f"Sequence {i+1}: Start codon found at position {location}")
        else:
            print(f"Sequence {i+1}: No start codon found")
    print("")
        

    

