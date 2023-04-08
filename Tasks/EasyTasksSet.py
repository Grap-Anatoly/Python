# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.
def twoSum(nums, target):

    stash = {}

    for i, val in enumerate(nums):

        req = target - val

        if req in stash:
            return [stash[req], i]
        else:
            stash[val] = i

# nums = [1, 3, 4, 2]
nums = [3, 2, 1, 5, 8, 5, 10, 3]
target = 15

res = twoSum(nums, target)

print(res)

# Check if number a palindrome
# 13 > 31   = False
# 921 > 129 = False
# 121 > 121 = True
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    s = str(x)

    if s == s[::-1]:
        return True
    else:
        return False

res = isPalindrome(1221)

print(res)

# Convert roman input into normal numbers
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    roman = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")

    vals = [*s]
    res = 0

    for val in vals:
        for k, v in roman.items():
            if k == val:
                res += v

    return res

print(romanToInt("MCMXCIV"))


# find the longest common prefix
def longestCommonPrefix(strs):
    res = ""

    if "" in strs:
        return res
    else:
        minWord = min((word for word in strs if word), key=len)
        minWord = str(minWord)

        print(minWord)

        temp = ""

        for l in minWord:

            temp += l
            tempArr = []

            for w in strs:

                if w.startswith(temp):
                    tempArr.append(temp)

            print(tempArr)

            if len(tempArr) == len(strs):
                res = tempArr[0]

        return res

strs = [""]

res = longestCommonPrefix(strs)

print(res)

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

def isValid(s):

    allowed = ['()', '{}', '[]']

    while any(l in s for l in allowed):
        for br in allowed:
            s = s.replace(br, '')
    return not s

    # chunks, chunk_size = len(s), 2
    # s = [s[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
    #
    # allowed = set(["[]", "()", "{}"])
    #
    # if set(s) <= allowed:
    #     return True
    # else:
    #     return False


s = "()[]{]"

print(isValid(s))


# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
def mergeTwoLists(list1, list2):

    for i in list2:
        list1.append(i)

    return sorted(list1)


list1 = [1, 2, 4]
list2 = [1, 3, 4]

res = mergeTwoLists(list1, list2)

print(res)

# Remove Duplicates from Sorted Array
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def removeDuplicates(nums):

    # res = set(nums)
    # k = len(res)
    #
    # res = list(res)
    #
    # while len(res) != len(nums):
    #     res.append("_")
    #
    # return k, res

    nums = set(nums)
    k = len(nums)

    nums = list(nums)
    print(nums)

    return k


k = removeDuplicates(nums)

print(len(nums), nums)
print(k)

# Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place.
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
nums = [0, 1, 2, 2, 3, 0, 4, 2]

def removeElement(nums, val):

    for i in range(len(nums)):
        print(i)
        if nums[i] == val:
            nums[i] = "x"
            print(nums)

    while "x" in nums:
        nums.remove("x")

    print(nums)
    res = len(nums)

    return res

res = removeElement(nums, 2)

print(res)

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        return haystack.index(needle)

haystack = "leetcode"
needle = "leet0"

print(strStr(haystack, needle))


# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

def searchInsert(nums, target):

    pos = 0

    if target not in nums:
        for i in range(len(nums)):
            print(f"Pos {i}")
            if i == 0 and target < nums[i]:
                return i
            elif i == (len(nums) - 1) and target > nums[i]:
                return i + 1
            elif i != (len(nums)-1):
                if target > nums[i] and target < nums[i+1]:
                    return i + 1

    else:
        for n in nums:
            if n == target:
                return pos
            else:
                pos += 1


nums = [3, 4, 7, 9]
target = 0

print(searchInsert(nums, target))


# Given a string s consisting of words and spaces,
# return the length of the last word in the string.

def lengthOfLastWord(str):

    last = str.split()
    #last = last[-1]
    size = len(last[-1])

    return size


res = lengthOfLastWord("Hello world my name is Meee")

print(res)

# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.

def plusOne(digits):

    tempString = ""
    res = []

    for d in digits:
        tempString += str(d)

    number = int(tempString)
    number += 1

    for d in str(number):
        res.append(int(d))

    return res

digits = [1, 2, 3]

res = plusOne(digits)

print(res)

# Given two binary strings a and b, return their sum as a binary string.

def addBinary(a, b):

    binA = int(a, 2)
    binB = int(b, 2)

    res = bin(binA + binB)

    return res[2:]

a = "11"
b = "1"

res = addBinary(a, b)

print(res)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.

def mySqrt(x):

    if x <= 0:
        return 0
    else:
        res = 0
        oddN = 1

        while x - oddN >= 0:
            x = x - oddN
            res += 1
            oddN += 2

        # or simple usage of res = (x ** 0,5)
        return res


x = 8

res = mySqrt(x)

print(res)

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    res = 1
    if n != 1:
        a, b = 1, 1
        while res <= n:
            a, b = b, a + b
            res += 1
        return a
    else:
        return res

n = 4

res = climbStairs(n)

print(f"Choices: {res}")

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):

    c = head

    while c:
        while c.next and c.next.val == c.val:
            c.next = c.next.next
        c = c.next
    return head

# You are given two integer arrays nums1 and nums2,
# sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

def merge(nums1, m, nums2, n):

    while len(nums1) > m:
        nums1.pop()
    while len(nums2) > n:
        nums2.pop()

    for n in nums2:
        nums1.append(n)

    r = len(nums1)

    for i in range(r):
        for j in range(0, r - i - 1):
            if nums1[j] > nums1[j + 1]:
                nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]

    print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)