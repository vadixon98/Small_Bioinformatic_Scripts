# Problem 2.
# write a function that provides base complements

from aminoAcids import *

def compBase(N):
     '''takes a string that is a single DNA base "A", "G", "T", or "C" as input and returns the base that is complementary to it
     
     Args:
         N: Single DNA base character
         
     Returns:
         str: Complementary base, or 'N' for invalid bases
     '''
     # Input validation
     if not isinstance(N, str):
         raise TypeError("N must be a string")
     if len(N) != 1:
         raise ValueError("N must be a single character")
     
     N = N.upper()
     if N == 'A':
         return 'T'
     elif N == 'T':
         return 'A'
     elif N == 'C':
         return 'G'
     elif N == 'G':
         return 'C'
     else:
         return 'N'  # Return 'N' for invalid bases

# Problem 2 next smaller function
# Problem 2 reverse complementary DNA string

def reverse(s):
    '''takes in the string s and returns a string that is the reverse of s'''
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

# Problem 2 next smaller function
# Problem 2 reverse complementary DNA string

def reverseComplement(DNA):
    '''takes a DNA string as input (in 5' to 3' order) and returns the sequence of its complementary DNA strand, also in 5' to 3' order'''
    # Reverse the DNA string
    reversed_DNA = reverse(DNA)
    # Get the complementary bases
    comp_DNA = ''.join(compBase(N) for N in reversed_DNA)
    return comp_DNA

# Problem 2 amino codon function

def amino(codon):
    '''takes as input a codon string (a string of three letters) and returns the corresponding amino acid.
    
    Args:
        codon: Three-letter DNA codon string
        
    Returns:
        str: Single-letter amino acid code, or 'X' for unknown/invalid codons
    '''
    # Input validation
    if not isinstance(codon, str):
        raise TypeError("codon must be a string")
    if len(codon) != 3:
        raise ValueError(f"codon must be exactly 3 characters, got {len(codon)}")
    
    codon = codon.upper()
    # List of codons and their corresponding amino acids
    aa = ['F', 'L', 'I', 'M', 'V', 'S', 'P', 'T', 'A', 'Y', '|', 'H', 'Q', 'N', 'K', 'D', 'E', 'C', 'W', 'R', 'G']
    codons = [
        ['TTT', 'TTC'], ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], ['ATT', 'ATC', 'ATA'], ['ATG'],
        ['GTT', 'GTC', 'GTA', 'GTG'], ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], ['CCT', 'CCC', 'CCA', 'CCG'],
        ['ACT', 'ACC', 'ACA', 'ACG'], ['GCT', 'GCC', 'GCA', 'GCG'], ['TAT', 'TAC'], ['TAA', 'TAG', 'TGA'],
        ['CAT', 'CAC'], ['CAA', 'CAG'], ['AAT', 'AAC'], ['AAA', 'AAG'], ['GAT', 'GAC'], ['GAA', 'GAG'],
        ['TGT', 'TGC'], ['TGG'], ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], ['GGT', 'GGC', 'GGA', 'GGG']
    ]
    for i in range(len(aa)):
        if codon in codons[i]:
            return aa[i]
    return 'X'  # Return 'X' for unknown/invalid codons

# Problem 2 Final function, calling amino codon function to return amino acid string

def codingStrandToAA(DNA):
    '''takes a sequence of DNA nucleotides from the coding strand and returns the corresponding amino acids as a string'''
    DNA = DNA.upper()
    protein = ''
    # Only process complete codons (length must be multiple of 3)
    for i in range(0, len(DNA) - len(DNA) % 3, 3):
        codon = DNA[i:i+3]
        if len(codon) == 3:  # Only process complete codons
            protein += amino(codon)
    return protein


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

