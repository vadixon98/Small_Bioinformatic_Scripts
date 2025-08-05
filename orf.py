from dna import *

def restOfORF(DNA):
    """Takes a sequence starting with an ATG and finds first stop
    codon. Returns ORF. If no in-frame stop codon, return whole
    sequence."""
    for i in range(0,len(DNA),3):
        if DNA[i:(i+3)] in stopList:
            seq=DNA[:i]
            return seq
    return DNA

def oneFrame(DNA):
    """Begining at the start of DNA, searches that one frame for all
    ORFs. Returns their seqs as list."""
    seqL = []
    for i in range(0,len(DNA),3):
        if DNA[i:i+3] == "ATG":
            seq = restOfORF(DNA[i:])
            seqL = seqL + [seq]
    return seqL

def longestORF(DNA):
    """Finds the longest distance between a Start codon and the next
    in frame Stop. Returns this along with the corresponding DNA."""
    maxLn=0
    maxSeq=""
    for orf in oneFrame(DNA)+oneFrame(DNA[1:])+oneFrame(DNA[2:]):
        if len(orf)>maxLn:
            maxSeq=orf
            maxLn=len(orf)
    return(maxSeq)
