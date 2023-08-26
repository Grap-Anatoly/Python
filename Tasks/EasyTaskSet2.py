# You have a bomb to defuse, and your time is running out! Your informer will provide you with a
# circular array code of length of n and a key k.
#
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
#
# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
#
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
def decrypt(code, k):

    res = []
    for i in range(len(code)):
        if k > 0:
            temp = code[i + 1:] + code[:i]
            res.append(sum(temp[0: k]))
        if k < 0:
            temp = code[:i][::-1] + code[i:][::-1]
            res.append(sum(temp[0: abs(k)]))
        if k == 0:
            res.append(0)

    return res

# You are given an array of distinct integers arr and an array of integer arrays pieces,
# where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
#
# Return true if it is possible to form the array arr from pieces. Otherwise, return false.
def canFormArray(arr, pieces):

    counter = 0

    while counter < len(arr):
        for i in pieces:
            if i[0] == arr[counter]:

                n = len(i)

                if i != arr[counter:n + counter]:
                    continue
                counter += n
                pieces.remove(i)
                break
        else:
            return False
    return True

# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence.
# The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence.
# If word is not a substring of sequence, word's maximum k-repeating value is 0.
#
# Given strings sequence and word, return the maximum k-repeating value of word in sequence.
def maxRepeating(sequence, word):

    res = 0
    sub = word

    while len(sub) <= len(sequence):
        if sub in sequence:
            res += 1
        sub += word

    return res

# You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:
#
# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# Return the maximum integer in the array nums​​​.
def getMaximumGenerated(n):

    res = [0, 1]

    if n == 0:
        return 0
    else:
        for i in range(2, n + 1):
            if i % 2 == 0:
                res.append(res[i // 2])
            else:
                res.append(res[i // 2] + res[(i // 2) + 1])

        return max(res)

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
#
# A string is represented by an array if the array elements concatenated in order forms the string.
def arrayStringsAreEqual(word1, word2):

    return "".join(word1) == "".join(word2)

# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.
def countConsistentStrings(allowed, words):

    allowed = list(allowed)

    for i in range(len(words)):
        for j in words[i]:
            if j not in allowed:
                words[i] = ""

    res = 0

    for i in words:
        if i != "":
            res += 1

    return res

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money
# the i th customer has in the j th bank. Return the wealth that the richest customer has.
#
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
def maximumWealth(accounts):

    totalWealth = []
    for i in accounts:
        totalWealth.append(sum(i))

    return max(totalWealth)