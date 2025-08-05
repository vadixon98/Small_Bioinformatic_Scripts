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

def t_finder(some_list):
    ''' finds number of strings with >= 2 ts'''
    
    counter = 0
    
    for seq in some_list:
        num_ts = seq.count('t')
        if num_ts >= 2:
            counter = counter + 1

    return counter


def GC_maker(some_list):
    '''finds GC content of strings in a list'''  

    GC_results = []

    for seq in some_list:
        num_cs = seq.count('c')
        num_gs = seq.count('g')
        GC_count = num_cs + num_gs
        GC_results.append(GC_count)

    return GC_results


def GC_rich(some_list):
    '''finds GC rich strings in a list'''
    
    # this function uses the round() function
    # round() shortens a float to fewer digits

    GC_much = []

    for seq in some_list:
        num_cs = seq.count('c')
        num_gs = seq.count('g')
        GC_count = num_cs + num_gs
        GC_perc = 100 * (GC_count / len(seq))
        if GC_perc >= 55:
            GC_much.append(round(GC_perc,2))

    return GC_much


def string_start(seq):
    '''checks string for potential start codon'''

    got_start = 'no'
    start_location = 'none'

    for index in range(len(seq)+1):
        if seq[index:index+3] == 'atg':
            got_start = 'yes'
            start_location = index

    return got_start, start_location
            

def list_start(some_list):
    '''finds strings in list that may have a start codon'''

    start_results = []
    
    for seq in some_list:
        start_results.append(string_start(seq)) 

    return start_results


def seq_analyzer(some_list):
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
    print(list_start(some_list))
    print("")
        

    

