from typing import Union


def loadSeq(fileName: Union[str, bytes]) -> str:
    """Load sequence from a fasta file with a single entry.
    
    Args:
        fileName: Path to the FASTA file
        
    Returns:
        str: The DNA/protein sequence (without header)
        
    Raises:
        FileNotFoundError: If the file does not exist
        IOError: If there's an error reading the file
        ValueError: If the file is empty or has no sequence data
    """
    try:
        with open(fileName, "r") as f:
            linesL = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{fileName}' not found")
    except IOError as e:
        raise IOError(f"Error reading file '{fileName}': {e}")
    
    # Check if file is empty
    if len(linesL) == 0:
        raise ValueError(f"File '{fileName}' is empty")
    
    # combine lines, skipping first (header line)
    # Optimized: use join instead of string concatenation
    seq = ''.join(line.rstrip() for line in linesL[1:])
    
    # Check if we got any sequence data
    if len(seq) == 0:
        raise ValueError(f"No sequence data found in '{fileName}' (file may only contain header)")
    
    return seq
