# Problem 1a.

def countLength(dnaList, length):
    '''takes a list of DNA strings called DNAlist and a positive integer length as input and returns the number of strings in the list that have the specified length'''
    counter = 0
    for num in dnaList:
        if len(num) == length:
            counter = counter + 1
    return counter

dnaList = ['AAA', 'ACGAC','CG', 'TCA']

countLength(dnaList, 4)
0
countLength(dnaList,3)
2

# Problem 1b.

def getLength(DNAlist,length):
    '''takes a list of DNA strings called DNAlist and a positive integer length as input and returns a list of the strings of that length'''
    result = []
    for dna_string in DNAlist:
        if len(dna_string) == length:
            result.append(dna_string)
    return result

getLength(["ATA", "ATCG", "TTT", "A"], 3)
['ATA', 'TTT']

# Problem 1c.

def factorial(n):
    '''takes a positive integer n as input and returns n!'''
    counter = 1
    for i in range(1, n + 1):
        counter *= i
    return counter

factorial(1)
1
factorial(3)
6
factorial(4)
24

