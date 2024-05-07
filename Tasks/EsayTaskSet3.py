

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