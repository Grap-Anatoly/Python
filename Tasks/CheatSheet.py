"""
 Convert multidimensional list rows into columns

    1 2 3     1 4 7
    4 5 6  >  2 5 8
    7 8 9     3 6 9
"""


def rowsIntoColumns(list):
    res = []
    for j in range(len(list[0])):
        temp = []
        for i in list:
            temp.append(i[j])
        res.append(temp)


"""
 Returns list of Fibonacci sequence 
 (each number is the sum of the two preceding ones; starting from 0) 

    0 = 0
    1 = 1
    1 = 1 + 0
    2 = 1 + 1
    3 = 2 + 1
    5 = 3 + 2
    ...
    n = (n - 1) + (n - 2)
"""


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fibb = [0, 1]

    for i in range(n):
        prv = fibb[-2]
        nxt = fibb[-1]
        fibb.append(prv + nxt)

    return fibb


"""
 Check if sentence has target prefix in any of it`s words

    sentence = "i love eating burger"
    prefix = "burg"
    result: 4 (word with prefix)
"""


def hasPrefix(sentence, prefix):

    sentence = sentence.split(" ")

    for s in sentence:
        # Check if target prefix in word(s)
        # and check if its position is at the beginning of the word
        if prefix in s and prefix[0:len(prefix)] == s[0:len(prefix)]:
            return sentence.index(s) + 1

    return "There is no prefix in input sentence"


"""
 Dictionary of english alphabet with its positional numbers 
 as a keys

    Key = "a" > Number = 1
    Key = "c" > Number = 3
"""


letters = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
           "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
           "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

"""
 Greatest common divisor of 2 numbers
"""

def getDivisor(a, b):
    if (b == 0):
        return a
    else:
        return getDivisor(b, a % b)


"""
 Capitalize the string by changing the capitalization of each word such that:

    If the length of the word is 1 or 2 letters, change all letters to lowercase.
    Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
    
    capiTalIze tHe titLe > Capitalize The Title
    First leTTeR of EACH Word > First Letter of Each Word
"""


def capitalizeTitle(title):

    res = []
    title = title.split()

    for i in title:
        if len(i) <= 2:
            res.append(i.lower() + " ")
        else:
            i = i.lower()
            i = list(i)

            f = i[0]
            f = f.upper()
            i[0] = f

            res.append("".join(i) + " ")

    f = res[-1]
    f = f[0:-1]
    res[-1] = f

    return "".join(res)


"""
 Get list of all Excel indexes in range, represented as a string "<col><row>":
 
    <col> denotes the column number c of the cell. It is represented by alphabetical letters.
    For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
    <row> is the row number r of the cell. The rth row is represented by the integer r.

    Inputs are in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1,
    <row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2,
    
    Returns all items in given range/
    Input: s = "K1:L2"
    Output: ["K1","K2","L1","L2"]
    
    Input: s = "A1:F1"
    Output: ["A1","B1","C1","D1","E1","F1"]  
"""

def cellsInRange(s):

    letters = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
               "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
               "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    s = list(s)

    rows = [letters[s[0].lower()], letters[s[3].lower()]]
    cols = [int(s[1]), int(s[-1])]

    res = []
    for i in range(rows[0], rows[1] + 1):
        for j in range(cols[0], cols[1] + 1):
            res.append("%s%d" % (list(letters.keys())[list(letters.values()).index(i)].upper(), j))

    return res


"""
 Check if number is Prime:

    An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.

    Returns boolean value True or False
    
    Input: num = 4
    Output: False

    Input: num = -1
    Output: False
    
    Input: num = 11
    Output: True
"""

def isPrime(num):
    prime = False

    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return prime
        else:
            prime = True
            return prime
    else:
        return prime