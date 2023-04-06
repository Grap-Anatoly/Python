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




