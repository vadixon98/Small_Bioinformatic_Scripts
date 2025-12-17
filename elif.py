

def ORFadviser(dna):
    '''Takes a string called DNA as input and validates if it's an ORF.
    
    The function returns the string 'This is an ORF' if the input string satisfies all three of the conditions required of ORFs.
    Otherwise, if the first three symbols are not 'ATG', the function returns the string 'The first three bases are not ATG'.
    Otherwise, if the string does not end with 'TGA', 'TAG', or 'TAA', the function returns the string 'The last three bases are not a stop codon'.
    Otherwise, the function returns the string 'The string is not of the correct length.'
    
    Args:
        dna: DNA sequence string to validate
        
    Returns:
        str: Validation message
    '''
    # Input validation
    if not isinstance(dna, str):
        raise TypeError("dna must be a string")
    if len(dna) < 3:
        return 'The string is too short to be an ORF (minimum 3 bases required).'
    
    # Normalize to uppercase for comparison
    dna = dna.upper()
    
    if dna[:3] == 'ATG' and dna[-3:] in ('TGA', 'TAG', 'TAA') and len(dna) % 3 == 0:
        return 'This is an ORF.'
    elif dna[:3] != 'ATG':
        return 'The first three bases are not ATG.'
    elif dna[-3:] not in ('TGA', 'TAG', 'TAA'):
        return 'The last three bases are not a stop codon.'
    else:
        return 'The string is not of the correct length.'


def friendly(greeting):
    '''takes a string named greeting as input. If the greeting begins with the words 'Hello' or 'Hi', the function returns some friendly greeting string of your choice. Otherwise, if the greeting string ends with a question mark, the function returns the string 'Good question!'. Otherwise, the function returns with some string indicating that it didn't understand the greeting (e.g., 'I am sorry, but I did not understand you)'''
    if greeting.startswith('Hello') or greeting.startswith('Hi'):
        return "Hello, hope you are doing well!"
    elif greeting.endswith('?'):
        return "Good question!"
    else:
        return "I am sorry, but I did not understand you."
