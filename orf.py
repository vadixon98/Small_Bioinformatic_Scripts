from typing import List
from dna import *

# Constants - stop codons
STOP_CODONS: List[str] = ['TAA', 'TAG', 'TGA']
stopList = STOP_CODONS  # For backward compatibility


def restOfORF(DNA: str) -> str:
    """Takes a sequence starting with an ATG and finds first stop
    codon. Returns ORF. If no in-frame stop codon, return whole
    sequence."""
    for i in range(0, len(DNA), 3):
        if DNA[i:(i+3)].upper() in stopList:
            seq=DNA[:i]
            return seq
    return DNA

def oneFrame(DNA: str) -> List[str]:
    """Beginning at the start of DNA, searches that one frame for all
    ORFs. Returns their seqs as list.
    
    Args:
        DNA: DNA sequence string
        
    Returns:
        List of ORF sequences found in the frame
    """
    seqL = []
    for i in range(0, len(DNA), 3):
        if DNA[i:i+3].upper() == "ATG":
            seq = restOfORF(DNA[i:])
            seqL.append(seq)  # More efficient than list concatenation
    return seqL

def longestORF(DNA: str) -> str:
    """Finds the longest distance between a Start codon and the next
    in frame Stop. Returns this along with the corresponding DNA.
    
    Args:
        DNA: DNA sequence string to search
        
    Returns:
        Longest ORF sequence found across all three reading frames
    """
    # Optimized: collect all ORFs first, then find max (avoids multiple iterations)
    all_orfs = []
    for frame_offset in range(3):
        all_orfs.extend(oneFrame(DNA[frame_offset:]))
    
    if not all_orfs:
        return ""
    
    # Use max() with key function (more Pythonic and efficient)
    return max(all_orfs, key=len)
