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