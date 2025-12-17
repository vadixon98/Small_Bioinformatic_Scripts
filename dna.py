# Problem 2.
# write a function that provides base complements

from typing import Dict
from aminoAcids import *

# Constants - complement lookup dictionary (faster than if/elif chain)
COMPLEMENT_DICT: Dict[str, str] = {
    'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
    'a': 't', 't': 'a', 'c': 'g', 'g': 'c'
}

# Codon to amino acid dictionary (much faster than linear search)
CODON_TO_AA: Dict[str, str] = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'AGT': 'S', 'AGC': 'S', 'CCT': 'P', 'CCC': 'P',
    'CCA': 'P', 'CCG': 'P', 'ACT': 'T', 'ACC': 'T',
    'ACA': 'T', 'ACG': 'T', 'GCT': 'A', 'GCC': 'A',
    'GCA': 'A', 'GCG': 'A', 'TAT': 'Y', 'TAC': 'Y',
    'TAA': '|', 'TAG': '|', 'TGA': '|', 'CAT': 'H',
    'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAT': 'N',
    'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GAT': 'D',
    'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'TGT': 'C',
    'TGC': 'C', 'TGG': 'W', 'CGT': 'R', 'CGC': 'R',
    'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

# Translation table for reverse complement (fastest method)
COMPLEMENT_TRANSLATE = str.maketrans('ACGTacgtNn', 'TGCAtgcaNn')


def compBase(N: str) -> str:
    '''Takes a string that is a single DNA base "A", "G", "T", or "C" as input 
    and returns the base that is complementary to it.
    
    Args:
        N: Single DNA base character
        
    Returns:
        Complementary base, or 'N' for invalid bases
        
    Raises:
        TypeError: If N is not a string
        ValueError: If N is not a single character
    '''
    # Input validation
    if not isinstance(N, str):
        raise TypeError("N must be a string")
    if len(N) != 1:
        raise ValueError("N must be a single character")
    
    # Use dictionary lookup (O(1) vs O(n) for if/elif)
    return COMPLEMENT_DICT.get(N.upper(), 'N')


def reverse(s: str) -> str:
    '''Takes in the string s and returns a string that is the reverse of s.
    
    Args:
        s: String to reverse
        
    Returns:
        Reversed string
    '''
    # Use slice notation (much faster than loop)
    return s[::-1]


def reverseComplement(DNA: str) -> str:
    '''Takes a DNA string as input (in 5' to 3' order) and returns the sequence 
    of its complementary DNA strand, also in 5' to 3' order.
    
    Args:
        DNA: DNA sequence string
        
    Returns:
        Reverse complement of the DNA sequence
    '''
    # Optimized: use translate + reverse slice (fastest method)
    return DNA.translate(COMPLEMENT_TRANSLATE)[::-1]


def amino(codon: str) -> str:
    '''Takes as input a codon string (a string of three letters) and returns 
    the corresponding amino acid.
    
    Args:
        codon: Three-letter DNA codon string
        
    Returns:
        Single-letter amino acid code, or 'X' for unknown/invalid codons
        
    Raises:
        TypeError: If codon is not a string
        ValueError: If codon is not exactly 3 characters
    '''
    # Input validation
    if not isinstance(codon, str):
        raise TypeError("codon must be a string")
    if len(codon) != 3:
        raise ValueError(f"codon must be exactly 3 characters, got {len(codon)}")
    
    # Use dictionary lookup (O(1) vs O(n) for linear search)
    return CODON_TO_AA.get(codon.upper(), 'X')


def codingStrandToAA(DNA: str) -> str:
    '''Takes a sequence of DNA nucleotides from the coding strand and returns 
    the corresponding amino acids as a string.
    
    Args:
        DNA: DNA sequence string
        
    Returns:
        Amino acid sequence string
    '''
    DNA = DNA.upper()
    # Only process complete codons (length must be multiple of 3)
    # Use list comprehension + join (faster than string concatenation)
    codons = [DNA[i:i+3] for i in range(0, len(DNA) - len(DNA) % 3, 3) if len(DNA[i:i+3]) == 3]
    return ''.join(amino(codon) for codon in codons)


# Test code (run only when script is executed directly)
if __name__ == '__main__':
    # Test compBase
    assert compBase("A") == 'T'
    assert compBase("T") == 'A'
    
    # Test reverse
    assert reverse("spam") == 'maps'
    
    # Test reverseComplement
    assert reverseComplement("TTGAC") == 'GTCAA'
    
    # Test amino
    assert amino('ACC') == 'T'
    
    # Test codingStrandToAA
    assert codingStrandToAA("AGTCCCGGGTTT") == 'SPGF'
    assert codingStrandToAA("ATGCAACAGCTC") == 'MQQL'
    
    print("All tests passed!")
