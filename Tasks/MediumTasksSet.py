import math

# Given an integer array nums sorted in non-decreasing order,
# remove some duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.
def removeDuplicates(nums):
    numbers = {}
    for i in nums:
        if i in numbers:
            numbers[i] += 1
        else:
            numbers[i] = 1

    for k, v in numbers.items():
        while numbers[k] > 2:
            nums.pop(nums.index(k))
            numbers[k] -= 1


removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
def rotate(nums, k):

    rotate = nums[::-1]
    rotate = rotate[:k][::-1]

    nums = nums[:k + 1]

    return rotate + nums

def rotateSecond(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    while k != 0:

        last = nums[-1]
        temp = nums
        temp.pop()
        temp.insert(0, last)

        print(temp)

        for i in range(len(nums) - 1):
            nums[i] = temp[i]
        k -= 1

def rotateFast(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    while k != 0:
        last = nums[-1]

        nums.pop()
        nums.insert(0, last)

        k -= 1

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time. However,
# you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
def maxProfit(prices):
    res = []
    temp = []
    for i in range(len(prices)):
        if i < len(prices) - 1:
            if prices[i] < prices[i + 1]:
                temp.append(prices[i])
            else:
                temp.append(prices[i])
                res.append(temp)
                temp = []
        else:
            if prices[i] > prices[i - 1]:
                temp.append(prices[i])
                res.append(temp)

    profit = 0
    for r in res:
        if len(r) > 1:
            profit += max(r) - min(r)

    return profit

# You are given an integer array nums.
# You are initially positioned at the array's first index, and each element
# in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
def canJump(nums):
    end = len(nums) - 1

    for i in range(len(nums), 0, -1):
        if nums[i - 1] >= end - (i - 1):
            end = i - 1

    return end == 0

# Implement the RandomizedSet class:
#
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present.
# Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present.
# Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements
# (it's guaranteed that at least one element exists when this method is called).
# Each element must have the same probability of being returned.
class RandomizedSet:

    def __init__(self):
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.pop(self.data.index(val))
            return True
        else:
            return False

    # def getRandom(self) -> int:
    #     return self.data[randrange(len(self.data))]


# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].

# For small lists
def productExceptSelf(nums):
    res = []

    for i in range(len(nums)):
        temp = []
        temp = temp + nums
        temp.pop(i)

        product = 1
        for j in temp:
            product *= j

        res.append(product)

    return res

def productExceptSelfSymmetrical(nums):
    res = []

    for i in nums:
        left = nums[:i]
        right = nums[i + 1:]

        res.append(math.prod(left) * math.prod(right))

    return res

def productExceptSelfSuffPreff(nums):

    res = [1] * len(nums)
    left = 1
    right = 1

    for i in range(len(nums)):
        res[i] *= left
        left *= nums[i]

        res[-1 - i] *= right
        right *= nums[-1 - i]

    return res

print(productExceptSelf([1,2,3,4]))
print(productExceptSelfSymmetrical([1,2,3,4]))

# Given an integer, convert it to a roman numeral.
def intToRoman(num):
    res = ""
    roman = [[1000, "M"],
             [900, "CM"],
             [500, "D"],
             [400, "CD"],
             [100, "C"],
             [90, "XC"],
             [50, "L"],
             [40, "XL"],
             [10, "X"],
             [9, "IX"],
             [5, "V"],
             [4, "IV"],
             [1, "I"]]

    for i in range(len(roman)):
        while num >= roman[i][0]:
            res += roman[i][1]
            num -= roman[i][0]
            print(num)

    return res

# Given an input string s, reverse the order of the words.
def reverseWords(s):
    lst = s.split()
    res = ""

    for w in lst[::-1]:
        res += " " + w

    return res[1:]

# Given an integer n, return the number of trailing zeroes in n!.
def trailingZeroes(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    res = 0

    for i in str(fact)[::-1]:
        if i == "0":
            res += 1
        if int(i) > 0:
            break

    return res

def trailingZeroesByDivision(n):
    res = 0

    while n > 0:
        n = n // 5
        res = res + n

    return res

trailingZeroes(11)


def groupAnagramsForSmallLists(strs):
    res = []
    temp = []

    for s in strs:
        temp.append([s, sorted(list(s))])

    words = []
    for s in temp:

        counter = 0

        while counter < len(temp):
            if s[1] == temp[counter][1]:
                words.append(temp[counter][0])
            counter += 1

        if words not in res:
            res.append(words)

        words = []

    return res

def groupAnagrams(strs):

    wordsDict = {}

    for s in strs:
        key = "".join(sorted(s))
        if key in wordsDict:
            temp = wordsDict[key]
            temp.append(s)
            wordsDict[key] = temp
        else:
            wordsDict[key] = [s]

    res = []
    for k, v in wordsDict.items():
        res.append(v)

    return res[::-1]

groupAnagramsForSmallLists(["eat","tea","tan","ate","nat","bat"])


# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
def myPow(x, n):
    res = x
    if n > 0:
        for i in range(n - 1):
            res *= x
    else:
        for i in range(abs(n) + 1):
            res /= x

    return res

# Given a string s, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):

    check = {}
    left = 0
    res = 0

    for i in range(len(s)):
        if s[i] not in check:
            res = max(res, i - left + 1)
        else:
            if check[s[i]] < left:
                res = max(res, i - left + 1)
            else:
                left = check[s[i]] + 1
        check[s[i]] = i

    return res


# Given a string s, return the longest palindromic substring in s.
def longestPalindrome(s):

    if len(s) <= 1:
        return s

    ml = 1
    ms = s[0]
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if j - i + 1 > ml and s[i:j + 1] == s[i:j + 1][::-1]:
                ml = j - i + 1
                ms = s[i:j + 1]

    return ms


# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (
# you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
def convert(s, numRows):

    if numRows == 1:
        return s

    res = [""] * numRows
    add = 0
    inc = 1

    for i in s:
        res[add] += i

        if add == 0:
            inc = 1
        elif add == numRows - 1:
            inc = -1

        add += inc

    return "".join(res)

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
# the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
def reverse(x):

    x = list(str(x)[::-1])

    if x[-1] == "-":
        x.insert(0, "-")
        x.pop()

    x = int("".join(x))

    if -2 ** 31 < x and x < 2 ** 31 - 1:
        return x
    else:
        return 0

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
def threeSum(nums):

    res = set()
    nums = sorted(nums)[::-1]
    for i in range(len(nums) - 1):
        t = -nums[i]
        j = i + 1
        k = len(nums) - 1
        while j < k:

            if nums[j] + nums[k] == t:
                res.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            else:
                if nums[j] + nums[k] > t:
                    j += 1
                else:
                    k -= 1
    return res


# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
# closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
def threeSumClosest(nums, target):
    sums = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                sums.add(nums[i] + nums[j] + nums[k])

    sums = list(sums)
    res = min(sums, key=lambda x: abs(x - target))

    return res

def threeSumClosestTwoPointer(nums, target):

    closest = nums[0] + nums[1] + nums[2]
    nums = sorted(nums)

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s < target:
                left += 1
            else:
                right -= 1

            if abs(s - target) < abs(closest - target):
                closest = s

    return closest


# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
# could represent. Return the answer in any order.
def letterCombinations(digits):

    if len(digits) == 0:
        return digits

    letters = {"2": "abc",
               "3": "def",
               "4": "ghi",
               "5": "jkl",
               "6": "mno",
               "7": "pqrs",
               "8": "tuv",
               "9": "wxyz"}

    res = []
    curr = []

    def back(s):
        if s == len(digits):
            res.append("".join(curr))
        else:
            for l in letters[digits[s]]:
                curr.append(l)
                back(s + 1)
                curr.pop()

    back(0)

    return res

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
def generateParenthesis(n):

    res = {"()"}
    for i in range(n - 1):
        temp = set()
        for j in res:
            for k in range(len(j) + 1):
                temp.add(j[:k] + "()" + j[k:])
            res = temp

    return [i for i in res]

# Given an integer array nums, find the
# subarray
#  with the largest sum, and return its sum.
def maxSubArray(nums):

    mx = 0
    prevMx = -inf
    for i in nums:
        mx = max(i, mx + i)
        prevMx = max(prevMx, mx)
    return prevMx

# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
def permute(nums):

    if len(nums) == 1:
        return [nums[:]]

    res = []

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = self.permute(nums)

        for p in perms:
            p.append(n)

        res.extend(perms)
        nums.append(n)

    return res


# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
def merge(intervals):

    if len(intervals) <= 1:
        return intervals

    res = []
    counter = 0
    for i in range(len(intervals)):

        if counter < len(intervals) - 1:
            if intervals[counter][1] < intervals[counter + 1][0]:
                res.append(intervals[counter])
                counter += 1
            else:
                if intervals[counter][0] > intervals[counter + 1][0]:
                    res.append([intervals[counter + 1][0], max(intervals[counter][1], intervals[counter + 1][1])])
                    counter += 2
                elif intervals[counter][1] >= intervals[counter + 1][0]:
                    res.append([intervals[counter][0], max(intervals[counter][1], intervals[counter + 1][1])])
                    counter += 2

        else:
            if counter == len(intervals):
                return res
            else:
                res.append(intervals[counter])
                return res

def simpleMerge(intervals):

    res = []
    intervals = sorted(intervals)

    prev = intervals[0]

    for i in intervals[1:]:
        if i[0] <= prev[1]:
            prev[1] = max(prev[1], i[1])
        else:
            res.append(prev)
            prev = i

    res.append(prev)

    return res

# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.
def subsets(nums):
    res = []
    sub = []

    def createSubset(i):
        if i == len(nums):
            res.append(sub[:])
            return

        sub.append(nums[i])
        createSubset(i + 1)

        sub.pop()
        createSubset(i + 1)

    createSubset(0)
    return res

# You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.
#
# Return true if num is balanced, otherwise return false.
def isBalanced(num):

    even = 0
    odd = 0
    for i in range(len(num)):
        if i % 2 == 0:
            even += int(num[i])
        else:
            odd += int(num[i]) 

    return even == odd 