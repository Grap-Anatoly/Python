

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