

# You are given a 0-indexed string array words.
#
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
#
# isPrefixAndSuffix(str1, str2) returns true if str1 is both a
# prefix
#  and a
# suffix
#  of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix,
# but isPrefixAndSuffix("abc", "abcd") is false.
#
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i],
# words[j]) is true.
def countPrefixSuffixPairs(words):
    res = 0
    for i in range(len(words)):
        for j in range(len(words)):
            if i < j:
                if words[i] == words[j][:len(words)] and words[j].endswith(words[i]):
                    res += 1

    return res

# An ant is on a boundary. It sometimes goes left and sometimes right.
#
# You are given an array of non-zero integers nums. The ant starts reading nums from the first element of it to its
# end. At each step, it moves according to the value of the current element:
#
# If nums[i] < 0, it moves left by -nums[i] units.
# If nums[i] > 0, it moves right by nums[i] units.
# Return the number of times the ant returns to the boundary.
#
# Notes:
#
# There is an infinite space on both sides of the boundary.
# We check whether the ant is on the boundary only after it has moved |nums[i]| units. In other words, if the ant
# crosses the boundary during its movement, it does not count.
def returnToBoundaryCount(nums):

    pos = 0
    res = 0
    for i in nums:
        pos += i
        if pos == 0:
            res += 1

    return res

# You are given a 0-indexed string s typed by a user. Changing a key is defined as using a key different from the last
# used key. For example, s = "ab" has a change of a key while s = "bBBb" does not have any.
#
# Return the number of times the user had to change the key.
#
# Note: Modifiers like shift or caps lock won't be counted in changing the key that is if a user typed the letter 'a'
# and then the letter 'A' then it will not be considered as a changing of key.
#
#
def countKeyChanges(s):

    s = s.lower()
    res = 0

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            res += 1

    return res

# Given an array of integers called nums, you can perform the following operation while nums contains at least 2
# elements:
#
# Choose the first two elements of nums and delete them.
# The score of the operation is the sum of the deleted elements.
#
# Your task is to find the maximum number of operations that can be performed, such that all operations have
# the same score.
#
# Return the maximum number of operations possible that satisfy the condition mentioned above.
def maxOperations(nums):

    sums = []
    counter = 0
    for i in range(len(nums) // 2):
        if len(sums) == 0:
            sums.append(nums[counter] + nums[counter + 1])
            counter += 2
        else:
            if nums[counter] + nums[counter + 1] == sums[-1]:
                sums.append(nums[counter] + nums[counter + 1])
                counter += 2
            else:
                break

    return len(sums)

# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.
#
# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.
def triangleType(nums):

    nums = sorted(nums)

    if nums[0] + nums[1] > nums[2]:
        if len(set(nums)) == 1:
            return "equilateral"
        elif len(set(nums)) == 2:
            return "isosceles"
        else:
            return "scalene"
    else:
        return "none"

# You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2
# such that:
#
# nums1.length == nums2.length == nums.length / 2.
# nums1 should contain distinct elements.
# nums2 should also contain distinct elements.
# Return true if it is possible to split the array, and false otherwise.
def isPossibleToSplit(nums):

    for i in set(nums):
        if nums.count(i) > 2:
            return False

    return True

# Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make answer equal to
# matrix, then replace each element with the value -1 with the maximum element in its respective column.
#
# Return the matrix answer.
def modifiedMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                m = 0
                for k in range(len(matrix)):
                    m = max(m, matrix[k][j])
                matrix[i][j] = m

    return matrix

# You are given a 0-indexed integer array nums, and an integer k.
#
# In one operation, you can remove one occurrence of the smallest element of nums.
#
# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
def minOperations(nums, k):

    return len(nums) - len([i for i in nums if i >= k])


# You are given an array apple of size n and an array capacity of size m.
#
# There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a
# capacity of capacity[i] apples.
#
# Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.
#
# Note that, apples from the same pack can be distributed into different boxes.
def minimumBoxes(apple, capacity):
    capacity = sorted(capacity)[::-1]
    apples = sum(apple)

    res = 0
    while apples > 0:
        apples -= capacity[res]
        res += 1

    return res

# You are given a 1-indexed array of distinct integers nums of length n.
#
# You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first
# operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the ith operation:
#
# If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1. Otherwise,
# append nums[i] to arr2.
# The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and
# arr2 == [4,5,6], then result = [1,2,3,4,5,6].
#
# Return the array result.
def resultArray(nums):

    arr1 = [nums[0]]
    arr2 = [nums[1]]

    for i in range(2, len(nums)):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])

    return arr1 + arr2

# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each
# character.
def maximumLengthSubstring(s):

    subs = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subs.append(s[i:j])

    res = 0
    for i in subs:
        t = True
        for j in i:
            if i.count(j) > 2:
                t = False
        if t == True:
            res = max(res, len(i))

    return res

# Given a string s, find any substring of length 2 which is also present in the reverse of s.
# Return true if such a substring exists, and false otherwise.
def isSubstringPresent(s):

    subs = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(s[i:j]) == 2:
                subs.append(s[i:j][::-1])

    for i in subs:
        if i in s:
            return True

    return False


# You are given a string s representing a 12-hour format time where some of the digits (possibly none)
# are replaced with a "?".
#
# 12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59.
# The earliest 12-hour time is 00:00, and the latest is 11:59.
#
# You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting
# string is a valid 12-hour format time and is the latest possible.
#
# Return the resulting string.
def findLatestTime(s):

    s = list(s)

    if s[0] == s[1] and s[0] == "?":
        s[0] = "1"
        s[1] = "1"

    if s[0] == "?" and s[1] == "1" or s[0] == "?" and s[1] == "0":
        s[0] = "1"
    elif s[0] == "?":
        s[0] = "0"

    if s[1] == "?" and s[0] == '0':
        s[1] = "9"
    elif s[1] == "?" and s[0] == "1":
        s[1] = "1"

    if s[3] == "?":
        s[3] = "5"

    if s[4] == "?":
        s[4] = "9"

    return "".join(s)

# You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x)
# replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.
#
# Return the sum of encrypted elements.
def sumOfEncryptedInt(nums):

    res = []

    for i in nums:
        i = str(i)
        m = 0
        for j in i:
            m = max(m, int(j))

        temp = "%s" % m * len(i)
        res.append(int(temp))

    return sum(res)


# An integer divisible by the sum of its digits is said to be a Harshad number. You are given an integer x. Return
# the sum of the digits of x if x is a Harshad number, otherwise, return -1.
def sumOfTheDigitsOfHarshadNumber(x):

    digitSum = 0
    for i in str(x):
        digitSum += int(i)

    if x % digitSum == 0:
        return digitSum
    else:
        return -1

# You are given an array of integers nums. Return the length of the longest subarray of nums which is either
# strictly increasing or strictly decreasing.
def longestMonotonicSubarray(nums):

    subs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if len(nums[i:j]) == len(set(nums[i:j])):
                subs.append(nums[i:j])

    m = 0
    for i in subs:
        if i == sorted(i) or i == sorted(i)[::-1]:
            m = max(m, len(i))

    return m

# You are given a string s. The score of a string is defined as the sum of the absolute difference between the
# ASCII values of adjacent characters.
#
# Return the score of s.
def scoreOfString(s):

    sm = 0
    for i in range(len(s) - 1):
        sm += abs(ord(s[i]) - ord(s[i + 1]))

    return sm

# You are given an array nums of non-negative integers and an integer k.
#
# An array is called special if the bitwise OR of all of its elements is at least k.
#
# Return the length of the shortest special non-empty
# subarray
#  of nums, or return -1 if no special subarray exists.
def minimumSubarrayLength(nums, k):

    subs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subs.append(nums[i:j])

    m = 0
    for i in subs:
        temp = 0
        for j in range(len(i)):
            temp |= i[j]

        if temp >= k:
            if m == 0:
                m = len(i)
            else:
                m = min(m, len(i))

    if m != 0:
        return m
    else:
        return -1

# A word is considered valid if:
#
# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.
#
# Return true if word is valid, otherwise, return false.
#
# Notes:
#
# 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# A consonant is an English letter that is not a vowel.
def isValid(word):

    if len(word) < 3:
        return False

    for i in "@#$":
        if i in word:
            return False

    vowel = False
    vowels = "aeiou"
    for i in vowels:
        if i in word or i.upper() in word:
            vowel = True

    if vowel == False:
        return False

    consonant = False
    consonants = "qwrtypsdfghjklzxcvbnm"
    for i in consonants:
        if i in word or i.upper() in word:
            consonant = True

    if consonant == False:
        return False

    return True

# You are given two arrays of equal length, nums1 and nums2.
#
# Each element in nums1 has been increased (or decreased in the case of negative) by an integer, represented by the
# variable x.
#
# As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers
# with the same frequencies.
#
# Return the integer x.
def addedInteger(nums1, nums2):

    return min(nums2) - min(nums1)


# ou are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'. Character 'W' represents
# the white color, and character 'B' represents the black color.
#
# Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells
# are of the same color.
#
# Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.
#
#
def canMakeSquare(grid):

    squares = [[grid[0][0], grid[0][1], grid[1][0], grid[1][1]],
               [grid[0][1], grid[0][2], grid[1][1], grid[1][2]],
               [grid[1][0], grid[1][1], grid[2][0], grid[2][1]],
               [grid[1][1], grid[1][2], grid[2][1], grid[2][2]]]

    for i in squares:
        if i.count("B") >= 3 or i.count("W") >= 3:
            return True

    return False

# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
#
# Return the number of special letters in word.
def numberOfSpecialChars(word):

    res = 0
    for i in set(word.lower()):
        if i.lower() in word and i.upper() in word:
            res += 1

    return res


# You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.
#
# The permutation difference between s and t is defined as the sum of the absolute difference between the index of
# the occurrence of each character in s and the index of the occurrence of the same character in t.
#
# Return the permutation difference between s and t.
#
#
def findPermutationDifference(s, t):

    res = 0
    s = list(s)
    t = list(t)

    for i in s:
        res += abs(s.index(i) - t.index(i))

    return res


# You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:
#
# Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
# Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
# Return true if all the cells satisfy these conditions, otherwise, return false.
def satisfiesConditions(grid):

    if len(grid) == 1:
        for i in range(len(grid[0]) - 1):
            if grid[0][i] == grid[0][i + 1]:
                return False

        return True

    if len(grid[0]) == 1:
        if grid[0] == grid[1]:
            return True

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if i != len(grid) - 1:
                if grid[i][j] != grid[i + 1][j]:
                    return False
            else:
                if grid[i][j] != grid[i - 1][j]:
                    return False
            if j != len(grid[i]) - 1:
                if grid[i][j] == grid[i][j + 1]:
                    return False
            else:
                if grid[i][j] == grid[i][j - 1]:
                    return False

    return True


# You are given an array nums, where each number in the array appears either once or twice.
#
# Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.
def dulicateNumbersXOR(nums):

    xor = 0
    for i in set(nums):
        if nums.count(i) == 2:
            xor ^= i

    return xor

# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
#
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
def isArraySpecial(nums):

    if len(nums) == 1:
        return True

    for i in range(len(nums) - 1):
        if nums[i] % 2 == 0 and nums[i + 1] % 2 == 0:
            return False
        if nums[i] % 2 != 0 and nums[i + 1] % 2 != 0:
            return False

    return True

# You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive
# integer k.
#
# A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
#
# Return the total number of good pairs.
def numberOfPairs(nums1, nums2, k):

    res = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] % (nums2[j] * k) == 0:
                res += 1

    return res


# You are given a string s. Simulate events at each second i:
#
# If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
# If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
# Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting
# room given that it is initially empty.
def minimumChairs(s):

    res = []
    for i in s:
        if i == "E":
            if "" in res:
                res[res.index("")] = i
            else:
                res.append("E")
        else:
            res.pop(res.index("E"))
            res.append("")

    return len(res)

# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
#
# Return the minimum number of operations to make all elements of nums divisible by 3.
def minimumOperations(nums):

    res = 0
    for i in nums:
        if i % 3 != 0:
            res += 1

    return res

# You have an array of floating point numbers averages which is initially empty. You are given an array nums of n
# integers where n is even.
#
# You repeat the following procedure n / 2 times:
#
# Remove the smallest element, minElement, and the largest element maxElement, from nums.
# Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.
def minimumAverage(nums):

    avg = []
    nums = sorted(nums)
    for i in range(len(nums) // 2):
        avg.append((nums[0] + nums[-1]) / 2)
        nums.pop(0)
        nums.pop(-1)

    return min(avg)

# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its
# corresponding column number.
def titleToNumber(columnTitle):

    words = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11,
             "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
             "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

    res = 0
    counter = len(columnTitle) - 1
    for i in range(len(columnTitle)):
        res += words[columnTitle[i]] * 26 ** counter
        counter -= 1

    return res

# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length ==
# s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
#
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
def shortestToChar(s, c):

    res = []
    indexes = []
    for i in range(len(s)):
        if s[i] == c:
            indexes.append(i)

    for i in range(len(s)):
        temp = []
        for j in indexes:
            temp.append(abs(i - j))
        res.append(min(temp))
    return res

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only
# if the given words are sorted lexicographically in this alien language.
def isAlienSorted(words, order):

    enumerated = {}
    for i, letter in enumerate(order):
        enumerated[letter] = i

    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j >= len(words[i + 1]):
                return False
            if words[i][j] != words[i + 1][j]:
                if enumerated[words[i][j]] > enumerated[words[i + 1][j]]:
                    return False
                break

    return True

# The array-form of an integer num is an array representing its digits in left to right order.
#
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
def addToArrayForm(num, k):

    import sys
    sys.set_int_max_str_digits(100000)

    intNum = ""
    for i in num:
        intNum += str(i)

    newNum = str(int(intNum) + k)
    res = []
    for i in str(newNum):
        res.append(int(i))

    return res


# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left, return 0.
#
#
def lastStoneWeight(stones):

    stones = sorted(stones)[::-1]

    while len(stones) > 1:
        if stones[0] == stones[1]:
            stones.pop(0)
            stones.pop(0)
        else:
            t = stones[0] - stones[1]
            stones.pop(0)
            stones[0] = t
            stones = sorted(stones)[::-1]

    if stones != []:
        return stones[0]
    else:
        return 0


# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
#
# Choosing any x with 0 < x < n and n % x == 0.
# Replacing the number n on the chalkboard with n - x.
# Also, if a player cannot make a move, they lose the game.
#
# Return true if and only if Alice wins the game, assuming both players play optimally.
def divisorGame(n):

    return n % 2 == 0


# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do
# not appear in arr2 should be placed at the end of arr1 in ascending order.
def relativeSortArray(arr1, arr2):

    arr1Unique = []
    arr1Count = {}
    for i in arr1:
        if i not in arr2:
            arr1Unique.append(i)

    for i in arr2:
        arr1Count[i] = arr1.count(i)

    arr1Unique = sorted(arr1Unique)

    res = []
    for i in arr2:
        for j in range(arr1Count[i]):
            res.append(i)

    return res + arr1Unique


# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
def countCharacters(words, chars):

    res = 0
    for i in words:
        check = True
        for j in i:
            if i.count(j) > chars.count(j):
                check = False
                break
        if check == True:
            res += len(i)

    return res

# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
def dayOfYear(date):
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    res = 0
    if int(date[5:7]) != 1:
        for i in range(1, int(date[5:7])):
            if i == 2:
                if int(date[0:4]) % 400 == 0:
                    res += days[i] + 1
                elif int(date[0:4]) % 4 == 0 and int(date[0:4]) % 100 != 0:
                    res += days[i] + 1
                else:
                    res += days[i]
            else:
                res += days[i]

    res += int(date[8:10])

    return res


# We have n chips, where the position of the ith chip is position[i].
#
# We need to move all the chips to the same position. In one step, we can change the position of the ith chip from
# position[i] to:
#
# position[i] + 2 or position[i] - 2 with cost = 0.
# position[i] + 1 or position[i] - 1 with cost = 1.
# Return the minimum cost needed to move all the chips to the same position.
def minCostToMoveChips(position):

    even = 0
    odd = 0

    for i in position:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return min(even, odd)


# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
#
# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of
# two positive integers both smaller than it.)
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
def numPrimeArrangements(n):

    def isPrime(num):
        if num == 0 or num == 1:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
        else:
            return True

    p = []
    np = []

    for i in range(1, n + 1):
        if isPrime(i) == True:
            p.append(i)
        else:
            np.append(i)

    return math.factorial(len(p)) * math.factorial(len(np)) % (10 ** 9 + 7)

# You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
#
# In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams,
# and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies
# the conditions.
#
# Return words after performing all operations. It can be shown that selecting the indices for each operation in any
# arbitrary order will lead to the same result.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all
# the original letters exactly once. For example, "dacb" is an anagram of "abdc".
def removeAnagrams(words):

    res = []
    for i in range(0, len(words)):
        if i == 0 or sorted(words[i]) != sorted(words[i - 1]):
            res.append(words[i])

    return res

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two
# adjacent and equal letters and removing them.
#
# We repeatedly make duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
def removeDuplicates(s):

    res = []

    for i in s:
        if len(res) != 0:
            if res[-1] == i:
                res.pop()
            else:
                res.append(i)
        else:
            res.append(i)

    return "".join(res)

# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] =
# [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
#
# For each location indices[i], do both of the following:
#
# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all
# locations in indices.
def oddCells(m, n, indices):

    array = []
    for i in range(m):
        t = []
        for j in range(n):
            t.append(0)
        array.append(t)

    for i in indices:
        for j in range(len(array)):
            for k in range(len(array[j])):
                if j == i[0]:
                    array[j][k] += 1
                if k == i[1]:
                    array[j][k] += 1

    res = 0
    for i in array:
        for j in i:
            if j % 2 != 0:
                res += 1

# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that
# meet the following conditions:
#
# It has a length of k.
# It is a divisor of num.
# Given integers num and k, return the k-beauty of num.
#
# Note:
#
# Leading zeros are allowed.
# 0 is not a divisor of any value.
# A substring is a contiguous sequence of characters in a string.
def divisorSubstrings(num, k):

    res = 0
    num = str(num)
    for i in range(len(num) - k + 1):
        divisor = int(num[i:i + k])
        if divisor != 0:
            if int(num) % divisor == 0:
                res += 1

    return res

# You are given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic
# subsequence from s.
#
# Return the minimum number of steps to make the given string empty.
#
# A string is a subsequence of a given string if it is generated by deleting some characters of a given string
# without changing its order. Note that a subsequence does not necessarily need to be contiguous.
#
# A string is called palindrome if is one that reads the same backward as well as forward.
def removePalindromeSub(s):

    if s == s[::-1]:
        return 1
    else:
        return 2


# Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from
# 1 to n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector
# rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0]
# and ends at sector rounds[1]
#
# Return an array of the most visited sectors sorted in ascending order.
#
# Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction
# (See the first example).
def mostVisited(n, rounds):

    first = rounds[0]
    last = rounds[-1]

    if first <= last:
        return range(first, last + 1)
    else:
        return list(range(1, last + 1)) + list(range(first, n + 1))

# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds
# to visit all the points in the order given by points.
#
# You can move according to these rules:
#
# In 1 second, you can either:
# move vertically by one unit,
# move horizontally by one unit, or
# move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
# You have to visit the points in the same order as they appear in the array.
# You are allowed to pass through points that appear later in the order, but these do not count as visits.
def minTimeToVisitAllPoints(points):

    res = 0
    for i in range(len(points) - 1):
        xd = abs(points[i + 1][0] - points[i][0])
        yd = abs(points[i + 1][1] - points[i][1])

        res += max(xd, yd)

    return res

# You are given a string s. Reorder the string using the following algorithm:
#
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and
# append it to the result.
#
# Return the result string after sorting s with this algorithm.
def sortString(s):

    charsFreq = {}
    for i in s:
        if i in charsFreq:
            charsFreq[i] += 1
        else:
            charsFreq[i] = 1

    res = ""
    asc = True
    while any(charsFreq.values()) == True:
        if asc == True:
            for i in "abcdefghijklmnopqrstuvwxyz":
                if i in charsFreq and charsFreq[i] > 0:
                    res += i
                    charsFreq[i] -= 1
            asc = False
        else:
            for i in "abcdefghijklmnopqrstuvwxyz"[::-1]:
                if i in charsFreq and charsFreq[i] > 0:
                    res += i
                    charsFreq[i] -= 1
            asc = True

    return res

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east,
# or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
#
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have
# previously visited. Return false otherwise.
def isPathCrossing(path):

    coord = [[0, 0]]

    for i in path:
        if i == "N":
            last = list(coord[-1])
            last[0] += 1
            coord.append(last)
        if i == "E":
            last = list(coord[-1])
            last[1] += 1
            coord.append(last)
        if i == "S":
            last = list(coord[-1])
            last[0] -= 1
            coord.append(last)
        if i == "W":
            last = list(coord[-1])
            last[1] -= 1
            coord.append(last)

        if coord.count(coord[-1]) > 1:
            return True

    return False

# You are given an integer n.
#
# Each number from 1 to n is grouped according to the sum of its digits.
#
# Return the number of groups that have the largest size.
def countLargestGroup(n):

    dct = {}

    for i in range(1, n + 1):
        curr = sum(map(int, list(str(i))))

        if curr not in dct:
            dct[curr] = 1
        else:
            dct[curr] += 1

    print(dct)

    m = max(dct.values())

    return sum(1 for i in dct.values() if i >= m)


# Given an m x n binary matrix mat, return the number of special positions in mat.
#
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are
# 0 (rows and columns are 0-indexed).
def numSpecial(mat):

    res = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 1:

                column = True
                for k in range(len(mat)):
                    if k != i and mat[k][j] == 1:
                        column = False
                        break
                row = True
                if mat[i].count(1) > 1:
                    row = False

                if column == True and row == True:
                    res += 1

    return res

# There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water
# bottles from the market with one full water bottle.
#
# The operation of drinking a full water bottle turns it into an empty bottle.
#
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
def numWaterBottles(numBottles, numExchange):

    res = numBottles

    while numBottles >= numExchange:
        if numBottles % numExchange != 0:
            res += numBottles // numExchange
            numBottles = numBottles // numExchange + (numBottles % numExchange)
        else:
            res += numBottles // numExchange
            numBottles = numBottles // numExchange

    return res

# Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
# If multiple values have the same frequency, sort them in decreasing order.
#
# Return the sorted array.
def frequencySort(nums):

    dct = {}
    for i in set(nums):
        dct[i] = nums.count(i)

    nums.sort(reverse=True)
    nums.sort(key=lambda x: dct[x])

    return nums

# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points
# such that no points are inside the area.
#
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height).
# The widest vertical area is the one with the maximum width.
#
# Note that points on the edge of a vertical area are not considered included in the area.
def maxWidthOfVerticalArea(points):

    points = sorted(points)

    res = 0
    for i in range(len(points) - 1):
        res = max(res, points[i + 1][0] - points[i][0])

    return res

# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1
# respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.
#
# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack.
# At each step:
#
# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and
# leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
#
# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the
# i th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference
# of the j th student in the initial queue (j = 0 is the front of the queue).
# Return the number of students that are unable to eat.
def countStudents(students, sandwiches):

    for i in range(len(students) * 4):
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
        else:
            students.append(students[0])
            students.pop(0)

        if students == [] and sandwiches == []:
            break

    return len(students)

# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and
# lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However,
# "abA" is not because 'b' appears, but 'B' does not.
#
# Given a string s, return the longest substring of s that is nice. If there are multiple, return the
# substring of the earliest occurrence. If there are none, return an empty string.
def longestNiceSubstring(s):

    subs = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subs.append(s[i:j])

    res = []
    for i in subs:
        nice = True
        for j in i:
            if j == j.upper():
                if j.lower() not in i:
                    nice = False
            elif j == j.lower():
                if j.upper() not in i:
                    nice = False

        if nice == True:
            res.append(i)

    if res != []:
        return max(res, key=len)
    else:
        return ""

# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose
# two indices in a string (not necessarily different) and swap the characters at these indices.
#
# Return true if it is possible to make both strings equal by performing at most one string swap on
# exactly one of the strings. Otherwise, return false.
def areAlmostEqual(s1, s2):

    uneq = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            uneq += 1

    if uneq == 0 or uneq == 2:
        return sorted(s1) == sorted(s2)
    else:
        return False

# There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer.
# A character can only be typed if the pointer is pointing to that character.
# The pointer is initially pointing to the character 'a'.
def minTimeToType(word):

    res = len(word)
    pointer = "a"

    for i in word:
        diff = abs(ord(i) - ord(pointer))
        res += min(diff, 26 - diff)
        pointer = i

    return res

# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
#
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums.
#
# Note: Subsets with the same elements should be counted multiple times.
#
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
def subsetXORSum(nums):

    def getSubsets(lst):
        if len(lst) == 0:
            return [[]]
        subs = []
        for i in getSubsets(lst[1:]):
            subs += [i, i + [lst[0]]]
        return subs

    subs = getSubsets(nums)

    res = 0
    for i in subs:
        t = 0
        for j in i:
            t ^= j
        res += t

    return res


# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string)
# that is a non-empty substring of num, or an empty string "" if no odd integer exists.
#
# A substring is a contiguous sequence of characters within a string.
def largestOddNumber(num):

    import sys
    sys.set_int_max_str_digits(0)

    for i in range(len(num), -1, -1):
        s = num[:i + 1]
        if int(s) % 2 != 0:
            return s

    return ""

# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student.
# You are also given an integer k.
#
# Pick the scores of any k students from the array so that the difference between the highest and the
# lowest of the k scores is minimized.
#
# Return the minimum possible difference.
def minimumDifference(nums, k):

    if k <= 1:
        return 0
    else:
        nums = sorted(nums)
        res = nums[k - 1] - nums[0]

        for i in range(k, len(nums)):
            res = min(res, nums[i] - nums[i - k + 1])

        return res

# There are n availabe seats and n students standing in a room. You are given an array seats of length n,
# where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.
#
# You may perform the following move any number of times:
#
# Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position
# x to x + 1 or x - 1)
# Return the minimum number of moves required to move each student to a seat such that no two students
# are in the same seat.
#
# Note that there may be multiple seats or students in the same position at the beginning.
def minMovesToSeat(seats, students):

    seats = sorted(seats)
    students = sorted(students)

    res = 0
    for i in range(len(seats)):
        res += abs(students[i] - seats[i])

    return res

# A substring is a contiguous (non-empty) sequence of characters within a string.
#
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o',
# and 'u') and has all five vowels present in it.
#
# Given a string word, return the number of vowel substrings in word.
def countVowelSubstrings(word):

    vowel = "aeiou"

    subs = []
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            s = word[i:j]
            if len(s) >= 5:
                vow = True
                for l in s:
                    if l not in vowel:
                        vow = False
                if vow == True:
                    subs.append(word[i:j])

    res = 0
    for i in subs:
        if set(i) == set(vowel):
            res += 1

    return res

# Given an integer array hours representing times in hours, return an integer denoting the number of pairs i,
# j where i < j and hours[i] + hours[j] forms a complete day.
#
# A complete day is defined as a time duration that is an exact multiple of 24 hours.
#
# For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.
#
#
def countCompleteDayPairs(hours):

    res = []
    for i in range(len(hours)):
        for j in range(i, len(hours)):
            if i < j:
                if (hours[i] + hours[j]) % 24 == 0:
                    res.append([hours[i], hours[j]])

    return len(res)

# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum
# frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same
# degree as nums.
def findShortestSubArray(nums):

    mx = 0
    for i in set(nums):
        mx = max(nums.count(i), mx)

    mxValues = []
    for i in set(nums):
        if nums.count(i) == mx:
            mxValues.append(i)

    mn = len(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            s = nums[i:j]
            if len(s) >= mx:
                for m in mxValues:
                    if s.count(m) == mx:
                        mn = min(mn, len(s))

            if mn == mx:
                return mn

    return mn

def findShortestSubArrayFast(nums):

    d = {}
    for i, n in enumerate(nums):
        if n not in d:
            d[n] = [1, i, i]
        else:
            d[n][0] += 1
            d[n][2] = i

    m = 0
    mn = 0
    for v in d.values():
        if v[0] > m:
            m = v[0]
            mn = v[2] - v[1] + 1
        elif v[0] == m:
            mn = min(mn, v[2] - v[1] + 1)

    return mn


# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest
# triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
def largestTriangleArea(points):

    m = 0

    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for k in range(j + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]

                area = 1 / 2 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

                m = max(m, area)

    return m

# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal,
# otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the
# characters at s[i] and s[j].
#
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
def buddyStrings(s, goal):

    if len(s) != len(goal):
        return False
    else:
        if s == goal:
            f = False
            for i in s:
                if s.count(i) > 1:
                    f = True
            return f
        else:
            res = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    res.append(i)

            if len(res) > 2:
                return False

            return len(res) == 2 and s[res[0]] == goal[res[1]] and s[res[1]] == goal[res[0]]

# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
def isToeplitzMatrix(matrix):

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False

    return True


# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points
# are a boomerang.
#
# A boomerang is a set of three points that are all distinct and not in a straight line.
def isBoomerang(points):

    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    area = 1 / 2 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    return area != 0

# You are given a string s.
#
# Your task is to remove all digits by doing this operation repeatedly:
#
# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.
def clearDigits(s):

    m = []
    n = []
    for i in range(len(s)):
        if s[i] in '1234567890':
            n.append(i)
            p = i
            for j in range(len(s)):
                if s[p] in '1234567890':
                    p -= 1
                else:
                    if p in m:
                        p -= 1
                    else:
                        m.append(p)
                        break

    res = []
    s = list(s)

    for i in m:
        s[i] = ""

    for i in n:
        s[i] = ""

    return "".join(s)

# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down
# the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother).
# If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e.,
# the average of the four cells in the red smoother).
def imageSmoother(img):

    n = len(img)
    m = len(img[0])
    res = []
    for i in range(n):
        t = []
        for j in range(m):
            c = 1
            sm = img[i][j]
            if i - 1 >= 0 and j - 1 >= 0:
                sm += img[i - 1][j - 1]
                c += 1
            if j - 1 >= 0:
                sm = sm + img[i][j - 1]
                c += 1
            if i + 1 <= n - 1 and j - 1 >= 0:
                sm += img[i + 1][j - 1]
                c += 1
            if i + 1 <= n - 1:
                sm += img[i + 1][j]
                c += 1
            if i + 1 <= n - 1 and j + 1 <= m - 1:
                sm += img[i + 1][j + 1]
                c += 1
            if j + 1 <= m - 1:
                sm += img[i][j + 1]
                c += 1
            if i - 1 >= 0 and j + 1 <= m - 1:
                sm += img[i - 1][j + 1]
                c += 1
            if i - 1 >= 0:
                sm += img[i - 1][j]
                c += 1

            t.append(sm // c)
        res.append(t)
    return res

# A school is trying to take an annual photo of all the students. The students are asked to stand in a single
# file line in non-decreasing order by height. Let this ordering be represented by the integer array expected
# where expected[i] is the expected height of the ith student in line.
#
# You are given an integer array heights representing the current order that the students are standing in.
# Each heights[i] is the height of the ith student in line (0-indexed).
#
# Return the number of indices where heights[i] != expected[i].
def heightChecker(heights):

    sh = sorted(heights)
    res = 0
    for i in range(len(heights)):
        if sh[i] != heights[i]:
            res += 1

    return res

# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a
# tower of v cubes placed on top of cell (i, j).
#
# After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several
# irregular 3D shapes.
#
# Return the total surface area of the resulting shapes.
#
# Note: The bottom face of each shape counts toward its surface area.
def surfaceArea(grid):

    n = len(grid)
    res = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                res += 2 + grid[i][j] * 4
            if i > 0:
                res -= min(grid[i - 1][j], grid[i][j]) * 2
            if j > 0:
                res -= min(grid[i][j - 1], grid[i][j]) * 2

    return res

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is
# concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
def gcdOfStrings(str1, str2):

    res = ""
    if len(str1) >= len(str2):
        for i in range(len(str2)):
            t = str2[:i + 1]
            if len(str1) % len(t) == 0:
                l = len(str1) // len(t)
                l2 = len(str2) // len(t)
                if t * l == str1 and t * l2 == str2:
                    if len(t) > len(res):
                        res = t
    else:
        for i in range(len(str1)):
            t = str1[:i + 1]
            if len(str2) % len(t) == 0:
                l = len(str2) // len(t)
                l2 = len(str1) // len(t)
                if t * l == str2 and t * l2 == str1:
                    if len(t) > len(res):
                        res = t

    return res

# Given two strings first and second, consider occurrences in some text of the form "first second third",
# where second comes immediately after first, and third comes immediately after second.
#
# Return an array of all the words third for each occurrence of "first second third".
def findOcurrences(text, first, second):

    text = text.split(" ")
    res = []
    for i in range(len(text) - 2):
        if text[i] == first and text[i + 1] == second:
            res.append(text[i + 2])

    return res

# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the
# right.
#
# Note that elements beyond the length of the original array are not written. Do the above modifications to the
# input array in place and do not return anything.
def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    counter = 0
    while counter < len(arr) - 1:
        if arr[counter] == 0:
            t = arr[counter + 1]
            arr[counter + 1] = 0
            counter += 2
            for i in range(counter, len(arr)):
                t2 = arr[i]
                arr[i] = t
                t = t2
        else:
            counter += 1


# We distribute some number of candies, to a row of n = num_people people in the following way:
#
# We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to
# the last person.
#
# Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second
# person, and so on until we give 2 * n candies to the last person.
#
# This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach
# the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily
# one more than the previous gift).
#
# Return an array (of length num_people and sum candies) that represents the final distribution of candies.
def distributeCandies(candies, num_people):

    res = [0] * num_people
    counter = 0
    candy = 1

    while candies > 0:
        if counter < len(res):

            res[counter] += candy
            candy += 1

            left = candies - candy
            if left <= 0:
                if counter + 1 < len(res):
                    res[counter + 1] += candies - 1
                    break
                else:
                    res[0] += candies - 1
                    break
            else:
                counter += 1
                candies = left
        else:

            counter = 0
            res[counter] += candy
            candy += 1

            left = candies - candy
            if left < 0:
                if counter + 1 <= len(res):
                    res[counter + 1] += candies - 1
                    break
                else:
                    res[0] += candies - 1
                    break
            else:
                counter += 1
                candies = left

    return res


# Write a program to count the number of days between two dates.
#
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
def daysBetweenDates(date1, date2):

    res = 0

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if date1 > date2:
        date1, date2 = date2, date1

    y1, m1, d1 = date1.split("-")
    y2, m2, d2 = date2.split("-")

    y1, m1, d1, y2, m2, d2 = int(y1), int(m1), int(d1), int(y2), int(m2), int(d2)

    for i in range(y1, y2):
        res += 365
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            res += 1

    if y1 % 4 == 0 and y1 % 100 != 0 or y1 % 400 == 0:
        days[1] = 29
    else:
        days[1] = 28

    res -= sum(days[:m1 - 1]) + d1

    if y2 % 4 == 0 and y2 % 100 != 0 or y2 % 400 == 0:
        days[1] = 29
    else:
        days[1] = 28

    res += sum(days[:m2 - 1]) + d2

    return res


# You are given two strings current and correct representing two 24-hour times.
#
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59.
# The earliest 24-hour time is 00:00, and the latest is 23:59.
#
# In one operation you can increase the time current by 1, 5, 15, or 60 minutes.
# You can perform this operation any number of times.
#
# Return the minimum number of operations needed to convert current to correct.
def convertTime(current, correct):

    res = 0

    if current == correct:
        return res
    else:
        h1, m1 = current.split(":")
        h2, m2 = correct.split(":")

        h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)

        if m1 > m2:

            while h1 < h2 - 1:
                h1 += 1
                res += 1

            d = 60 - m1 + m2

            while d != 0:
                if d % 15 == 0:
                    d -= 15
                    res += 1
                elif d % 5 == 0:
                    d -= 5
                    res += 1
                else:
                    d -= 1
                    res += 1
        else:

            while h1 < h2:
                h1 += 1
                res += 1

            d = m2 - m1

            while d != 0:
                if d % 15 == 0:
                    d -= 15
                    res += 1
                elif d % 5 == 0:
                    d -= 5
                    res += 1
                else:
                    d -= 1
                    res += 1

        return res

# There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is
# represented by colors[i]:
#
# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from
# its left and right tiles) is called an alternating group.
#
# Return the number of alternating groups.
#
# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
def numberOfAlternatingGroups(colors):
    res = 0
    for i in range(len(colors)):
        if i == 0:
            if colors[-1] != colors[i] and colors[i] != colors[i + 1]:
                res += 1
        elif i == len(colors) - 1:
            if colors[0] != colors[i] and colors[i] != colors[i - 1]:
                res += 1
        else:
            if colors[i - 1] != colors[i] and colors[i] != colors[i + 1]:
                res += 1

    return res

# You are given a string s and an integer k. Encrypt the string using the following algorithm:
#
# For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).
# Return the encrypted string
def getEncryptedString(s, k):

        if len(set(s)) == 1:
            return s
        else:
            res = []
            for i in range(len(s)): 
                res.append(s[(i+k) % len(s)])
            
            return "".join(res)


# You are given two integers red and blue representing the count of red and blue colored balls. 
# You have to arrange these balls to form a triangle such that the 1st row will have 1 ball, the 2nd row will have 2 balls, 
# the 3rd row will have 3 balls, and so on.
# 
# All the balls in a particular row should be the same color, and adjacent rows should have different colors.
# 
# Return the maximum height of the triangle that can be achieved.
def maxHeightOfTriangle(red, blue):

        resR = 0
        resB = 0

        r1 = red
        r2 = red
        b1 = blue
        b2 = blue

        counter = 1
        redCheck = True
        for i in range(max(r1,b1)):
            if redCheck == True:
                if r1 < counter: 
                    break
                else:
                    resR += 1
                    r1 -= counter
                    counter += 1
                    redCheck = False
            else:
                if b1 < counter:
                    break
                else:
                    resR += 1
                    b1 -= counter
                    counter += 1
                    redCheck = True

        counter = 1
        blueCheck = True
        for i in range(max(r2,b2)):
            if blueCheck == True:
                if b2 < counter: 
                    break
                else:
                    resB += 1
                    b2 -= counter
                    counter += 1
                    blueCheck = False
            else:
                if r2 < counter:
                    break
                else:
                    resB += 1
                    r2 -= counter
                    counter += 1
                    blueCheck = True

        return max(resR, resB)

# Given a string s containing only digits, return the
# lexicographically smallest string
#  that can be obtained after swapping adjacent digits in s with the same parity at most once.
#
# Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4,
# have the same parity, while 6 and 9 do not.
def getSmallestString(s):
    s = list(s)

    for i in range(len(s) - 1):
        if int(s[i]) % 2 == 0 and int(s[i + 1]) % 2 == 0:
            temp = list(s)
            t = temp[i]
            temp[i] = temp[i + 1]
            temp[i + 1] = t
            if temp < s:
                return "".join(temp)
        if int(s[i]) % 2 != 0 and int(s[i + 1]) % 2 != 0:
            temp = list(s)
            t = temp[i]
            temp[i] = temp[i + 1]
            temp[i + 1] = t
            if temp < s:
                return "".join(temp)

    return "".join(s)


# You are given two positive integers n and k.
# 
# You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.
# 
# Return the number of changes needed to make n equal to k. If it is impossible, return -1.
def minChanges(n, k):

        res = 0
        bN = list(bin(n)[2:])
        bK = list(bin(k)[2:])

        if len(bK) < len(bN):
            while len(bK) < len(bN): 
                bK.insert(0, '0')

        for i in range(len(bN)):
            if bK[i] != bN[i]:
                bN[i] = '0'
                res += 1

        if bN == bK:
            return res
        else:
            return -1


# You are given two positive integers x and y, denoting the number of coins with values 75 and 10 respectively.
#
# Alice and Bob are playing a game. Each turn, starting with Alice, the player must pick up coins with a total value 115. 
# If the player is unable to do so, they lose the game.
#
# Return the name of the player who wins the game if both players play optimally.
def losingPlayer(x, y):

    if min(x,y // 4) % 2 == 0:
        return "Bob"
    else:
        return "Alice"

# You are given an array of positive integers nums.
# 
# Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit numbers 
# from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the 
# sum of Bob's numbers.
# 
# Return true if Alice can win this game, otherwise, return false.
def canAliceWin(nums):

    nums = sorted(nums)
    d = []
    s = []
    for i in range(len(nums)):
        if len(str(nums[i])) == 1:
            s.append(nums[i])
        else:
            d = nums[i:]
            break

   return sum(s) != sum(d)

# You are given an integer n representing the number of players in a game and a 2D array pick where pick[i] = [xi, yi] 
# represents that the player xi picked a ball of color yi.
# 
# Player i wins the game if they pick strictly more than i balls of the same color. In other words,
# 
# Player 0 wins if they pick any ball.
# Player 1 wins if they pick at least two balls of the same color.
# ...
# Player i wins if they pick at leasti + 1 balls of the same color.
# Return the number of players who win the game.
# 
# Note that multiple players can win the game.
def winningPlayerCount(n, pick):

balls = {}
    for i in pick:
        if i[0] in balls:
            balls[i[0]] += [i[1]]
        else:
            balls[i[0]] = [i[1]]
        
     res = 0
     for k, v in balls.items():
        for i in v:
            if v.count(i) > k:
                res += 1
                break
        
     return res


# You are given a binary string s and an integer k.
# 
# A binary string satisfies the k-constraint if either of the following conditions holds:
# 
# The number of 0's in the string is at most k.
# The number of 1's in the string is at most k.
# Return an integer denoting the number of substrings of s that satisfy the k-constraint.
def countKConstraintSubstrings(s, k):

    res = 0
        
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if sub.count("0") <= k or sub.count("1") <= k: 
                res += 1
        
    return res


# You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square on an 8 x 8 chessboard.
# 
# Return true if these two squares have the same color and false otherwise.
# 
# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), 
# and the number second (indicating its row).
def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

    letters = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

    cord1 = int(coordinate1[1]) + letters[coordinate1[0]]
    cord2 = int(coordinate2[1]) + letters[coordinate2[0]]

    if cord1 % 2 == 0 and cord2 % 2 == 0:
        return True
    elif cord1 % 2 != 0 and cord2 % 2 != 0:
        return True
    else:
        return False      	

# You are given an integer array nums, an integer k, and an integer multiplier.
# 
# You need to perform k operations on nums. In each operation:
# 
# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.
def getFinalState(nums, k, multiplier):

    for i in range(k):
        m = min(nums)
        pos = nums.index(m)
        nums[pos] = m * multiplier
        
    return nums

# You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.
#
# date can be written in its binary representation obtained by converting year, month, and day to their binary 
# representations without any leading zeroes and writing them down in year-month-day format.
# 
# Return the binary representation of date.
def convertDateToBinary(date):

    date = date.split("-")
    conv = []
    for i in date:
        conv.append(bin(int(i))[2:])
        conv.append("-")

    return "".join(conv)[:-1]

# You are given three positive integers num1, num2, and num3.
# 
# The key of num1, num2, and num3 is defined as a four-digit number such that:
# 
# Initially, if any number has less than four digits, it is padded with leading zeros.
# The ith digit (1 <= i <= 4) of the key is generated by taking the smallest digit among the ith digits of num1, num2, and num3.
# Return the key of the three numbers without leading zeros (if any).
def generateKey(num1, num2, num3):

    nums = [num1, num2, num3]
    res = []
    
    for i in range(len(nums)):
        n = str(nums[i])
        while len(n) < 4:
            n = "0" + n
        nums[i] = n
    
    for i in range(4):
        res.append(min(nums[0][i], nums[1][i], nums[2][i]))

    return int("".join(res))

# In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. 
# Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.
# 
# As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.
def getSneakyNumbers(nums):

    res = []
    for i in set(nums):
        if nums.count(i) == 2:
            res.append(i)
        if len(res) == 2:
            return res

# There are n mountains in a row, and each mountain has a height. You are given an integer array height where height[i] 
# represents the height of mountain i, and an integer threshold.
# 
# A mountain is called stable if the mountain just before it (if it exists) has a height strictly greater than threshold. 
# Note that mountain 0 is not stable.
# 
# Return an array containing the indices of all stable mountains in any order.
def stableMountains(height, threshold):

    res = []
    for i in range(1, len(height)):
        if height[i-1] > threshold:
            res.append(i)
        
    return res


# Alice and Bob are playing a game. Initially, Alice has a string word = "a".
# 
# You are given a positive integer k.
# 
# Now Bob will ask Alice to perform the following operation forever:
# 
# Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
# For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
# 
# Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
def kthCharacter(k):

    letters = list("abcdefghijklmnopqrstuvwxyz")
    string = ["a"]

    while len(string) < k:
        t = list(string)
        for i in range(len(string)):
            t.append(letters[letters.index(string[i])+1])
        string = t
    
    return string[k-1]

# You are given an array nums consisting of n prime integers.
# 
# You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and 
# ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].
# 
# Additionally, you must minimize each value of ans[i] in the resulting array.
# 
# If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.
def minBitwiseArray(nums):

    res = []
    for i in nums:
        t = []
        for j in range(i+1):
            if (j ^ (j + 1)) == i:
                t.append(j)
                break
        if len(t) == 0:
            res.append(-1)
        else:
            res.append(t[-1]) 
    
    return res

# You are given an integer array nums.
# 
# You replace each element in nums with the sum of its digits.
# 
# Return the minimum element in nums after all replacements.
def minElement(nums):
    
    res = max(nums)
    for i in nums:
        t = 0
        for j in str(i):
            t += int(j)
        res = min(res,t)
    
    return res

# You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.
def smallestNumber(n, t):
    while self.product(n) % t != 0:
        n += 1
    return n

def product(self, n):
    prod = 1
    while n > 0:
        prod *= n % 10
        n //= 10
    return prod


# Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.
#
# Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.
#
# You are given a string word, which represents the final output displayed on Alice's screen.
# 
# Return the total number of possible original strings that Alice might have intended to type.
def possibleStringCount(word):
    
    res = 0
    prev = ""
    for i in word:
        if i == prev:
            res += 1
        prev = i
    return res + 1

# You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.
# Return the minimum sum of such a subarray. If no such subarray exists, return -1.
# A subarray is a contiguous non-empty sequence of elements within an array.
def minimumSumSubarray(nums, l, r):

    res = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            sub = nums[i:j]
            if len(sub) >= l and len(sub) <= r:
                if sum(sub) > 0:
                    res.append(sum(sub))

    if len(res) > 0:
        return min(res) 
    else:
        return -1

# You are given a positive number n.
#
# Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits.
# 
# A set bit refers to a bit in the binary representation of a number that has a value of 1.
def smallestNumber(n):

    counter = n
    while set(str(bin(counter)[2:])) != set(str(1)):
        counter += 1

    return counter

# Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.
#
# Alice starts by removing exactly 10 stones on her first turn.
# For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
# The player who cannot make a move loses the game.
# 
# Given a positive integer n, return true if Alice wins the game and false otherwise.
def canAliceWin(n):

    turn = 0
    stones = 10

    while n >= stones:
        turn += 1
        n -= stones
        stones -= 1

    if turn == 0:
        return False
    else:
        if turn % 2 == 0:
            return False
        else:
            return True

# There is a snake in an n x n matrix grid and can move in four possible directions. Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j.
# 
# The snake starts at cell 0 and follows a sequence of commands.
# 
# You are given an integer n representing the size of the grid and an array of strings commands where each command[i] is either "UP", "RIGHT", "DOWN", and "LEFT". It's guaranteed that the snake will remain within the grid boundaries throughout its movement.
# 
# Return the position of the final cell where the snake ends up after executing commands.
def finalPositionOfSnake(n, commands):

    grid = []
    counter = 0
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(counter)
            counter += 1
        grid.append(temp)

    res = [0,0]

    for i in commands:
        if i == "UP":
            res[0] -= 1
        elif i == "RIGHT":
            res[1] += 1
        elif i == "DOWN":
            res[0] += 1
        else:
            res[1] -= 1

    return grid[res[0]][res[1]]