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

# Binary Tree Traversal
def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []


def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []

# Given the roots of two binary trees p and q,
# write a function to check if they are the same or not.

def isSameTree(p, q):
    tree1 = []
    tree2 = []

    if p and q:
        while p:
            tree1.append(p.val)
            p = p.left
        while q:
            tree2.append(q.val)
            q = q.left

        if tree1 == tree2:
            return True
        else:
            return False
    elif p and not q:
        return False
    elif q and not p:
        return False
    else:
        return True

# simple
def isSameTreeSimple(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q

# tuple
def isSameTreeTuple(self, p, q):
    def t(n):
        return n and (n.val, t(n.left), t(n.right))
    return t(p) == t(q)

# get max depth of binary tree
def maxDepth(root):

    def counter(root, depth):
        if not root:
            return depth
        else:
            return max(counter(root.left, depth + 1), counter(root.right, depth + 1))

    return counter(root, 0)

# Given an integer numRows, return the first numRows of Pascal's triangle.
def generate(numRows):
    res = [[1] * (i + 1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1, i):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res

n = 5

res = generate(n)

print(res)

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
def getRow(rowIndex):
    res = []
    one = [1]

    for i in range(rowIndex):

        res.append(one)

        temp = one
        temp.insert(len(one)+1, 0)
        temp = temp[::-1]

        for k in range(len(temp)):
            one[k] = one[k] + temp[k]

    return one

n = 3

result = getRow(n)

print(result)

# You are given an array prices where prices[i] is the price of a given stock
# on the ith day.
def maxProfit(prices):
    buy = 0
    sell = 1
    max_profit = 0
    while sell < len(prices):
        currentProfit = prices[sell] - prices[buy]  # our current Profit
        if prices[buy] < prices[sell]:
            max_profit = max(currentProfit, max_profit)
        else:
            buy = sell
        sell += 1
    return max_profit


prices = [7,1,5,3,6,4]

result = maxProfit(prices)

print(result)

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

def isValidPalindrome(s):

    acceptable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    res = ""

    for symb in s:
        if symb in acceptable:
            res += symb

    print(res)

    if res.lower() == res[::-1].lower():
        return True
    else:
        return False

# s = "A man, a plan, a canal: Panama"
s = "9,8"

res = isValidPalindrome(s)

print(res)

# Given a non-empty array of integers nums, every element appears twice except for one.
#
# Find that single one.
def singleNumber(nums):

    for n in nums:
        count = 0
        for k in nums:
            if n == k:
                count += 1
        if count != 2:
            return n

def singleNUmberFast(nums):
    xor = 0
    for num in nums:
        xor ^= num

    return xor

nums = [4,1,2,1,2]

res = singleNUmberFast(nums)

print(res)

# binary tree preorder traversion
def preorderTraversal(root):
    if root:
        return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)
    else:
        return []

# binary tree postorder traversion
def postorderTraversal(root):
    if root:
        return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]
    else:
        return []

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.
def getIntersectionNode(headA, headB):

    if headA is None or headB is None:
        return "No intersection"

    hA = headA
    hB = headB

    while hA != hB:
        hA = headB if hA is None else hA.next
        hB = headA if hB is None else hB.next

    return hA

# Given an integer columnNumber,
# return its corresponding column title as it appears in an Excel sheet.
def convertToTitle(columnNumber):

    res = ''

    while (columnNumber > 0):
        columnNumber -= 1
        res = chr(columnNumber % 26 + 65) + res
        columnNumber //= 26
    return res

# Given an array nums of size n, return the majority element.
def majorityElement(nums):

    count = {}

    for n in nums:
        c = 0
        for k in nums:
            if n == k:
                c += 1
            count[n] = c

    return max(count, key=count.get)

    # Faster method Via usage of set
    # srt = sorted(nums)
    # unique = set(srt)
    # count = {}
    #
    # print(unique)
    #
    # for n in unique:
    #     c = 0
    #     for k in srt:
    #         if n == k:
    #             c += 1
    #         count[n] = c
    #
    # return max(count, key=count.get)

nums = [2, 2, 1, 1, 1, 2, 2]

res = majorityElement(nums)

print(res)

# Write a function that takes the binary representation of an unsigned integer and returns the number of '1'
# bits it has (also known as the Hamming weight).

def hammingWeight(n):

    b = '{0:b}'.format(n)
    c = 0

    for n in b:
        if n == "1":
            c += 1

    return c


# Reverse bits of a given 32 bits unsigned integer.
def reverseBits(n):

    b = '{:032b}'.format(n)
    b = b[::-1]
    res = int(b, 2)

    return res

def isHappy(n):

    target = 1

    if n == 1 or n == 7:
        return True
    else:

        for r in range(9):
            s = []
            num = str(n)
            for i in num:
                s.append(int(i))
            for j in range(len(s)):
                s[j] = s[j] ** 2
            n = 0
            for k in s:
                n += k

        if target == n:
            return True
        else:
            return False




n = 19

print(isHappy(n))

# Remove elements form linked list
def removeLinked(head, val):
    temp = ListNode(-1)
    temp.next = head

    curr = temp
    while curr.next != None:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return temp.next


# Isomorphic Strings
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    else:
        if len(set(s)) == len(set(zip(s,t))) == len(set(t)):
            return True
        else:
            return False


s = "paper"
t = "title"

print(isIsomorphic(s, t))

# Reverse linked list
def reverseList(head):

    if head is None:
        return head
    else:
        prev = None
        #
        curr = head
        # 1, 2, 3, 4, 5
        while curr:
            next = curr.next
            # 2 - 3 - 4 - 5 - 1
            curr.next = prev
            #   - 1 - 2 - 3 - 4

            prev = curr
            # 1 - 2 - 3 - 4 - 5
            curr = next
            # 2 - 3 - 4 - 5 - 1

        return prev

# if list contains duplicates

def containsDuplicate(nums):
    s = set(nums)

    if len(s) != len(nums):
        return True
    else:
        return False

def containsNearbyDuplicate(nums, k):

    vals = {}
    for i, v in enumerate(nums):
        if v in vals and i - vals[v] <= k:
            return True
        vals[v] = i
    return False

nums = [1,2,3,1,2,3]
k = 2

print(containsNearbyDuplicate(nums, k))

# Implement stack using queues
class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        l = len(self.stack)
        self.stack.insert(l + 1, x)

    def pop(self) -> int:
        l = len(self.stack)
        res = self.stack[l-1]
        self.stack.pop(l-1)
        return res

    def top(self) -> int:
        l = len(self.stack)
        return self.stack[l-1]

    def empty(self) -> bool:
        l = len(self.stack)
        if l > 0:
            return False
        else:
            return True

# Summary ranges of the list
def summaryRanges(nums):
    res = []

    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        for n in nums:
            res.append(f"{n}")
            return res
    else:
        fill = []
        dct = {}

        for i in range(nums[-1] + 1):
            fill.append(i)

        count = 0
        for n in fill:
            if n in nums:
                dct[count] = n
            else:
                count = n + 1

        for k, v in dct.items():
            if k != v:
                res.append(f"{k}->{v}")
            else:
                res.append(f"{v}")

        return res

# for very big numbers(faster)
def fastSummaryRanges(nums):
    ranges = []
    res = []
    for n in nums:
        if not ranges or n > ranges[-1][-1] + 1:
            ranges += [],
        ranges[-1][1:] = n,

    for r in ranges:
        if len(r) > 1:
            res.append(f"{r[0]}->{r[-1]}")
        else:
            res.append(f"{r[0]}")
    return res


nums = [0,2,3,4,6,8,9,10,12,16,17]
# nums = [0,1,2,4,5,7]


print(fastSummaryRanges(nums))

def isPowerOfTwo(num):
    for x in range(1000):
        if num == 2 ** x:
            return True
    return False

    # if n == 0:
    #     return False
    # else:
    #     while n % 2 == 0:
    #         n /= 2
    #     return n == 1


print(isPowerOfTwo(256))

#  Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> int:
        res = self.l[0]
        self.l.pop(0)
        return res

    def peek(self) -> int:
        return self.l[0]

    def empty(self) -> bool:
        if len(self.l) == 0:
            return True

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

def isPalindrome(head):

    straight = []
    reverse = []

    while head:
        reverse = [head.val] + reverse
        straight.append(head.val)
        head = head.next

    return reverse == straight

# faster approach
def isPalindromeFast(head):

    l = []

    while head:
        l.append(head.val)
        head = head.next

    return l == l[::-1]

# words are an anagram
def isAnagram(s, t):

    if sorted(list(s)) == sorted(list(t)):
            return True

# binary tree path
def binaryTreePaths(root):
    res = []

    def findPath(node, path):
        if not node.left and not node.right:
            res.append(path)

        if node.left:
            findPath(node.left, path + "->" + str(node.left.val))

        if node.right:
            findPath(node.right, path + "->" + str(node.right.val))

    findPath(root, str(root.val))

    return res

# Given an integer num,
# repeatedly add all its digits until the result has only one digit, and return it.
def addDigits(num):

    s = str(num)
    temp = 0

    while len(s) != 1:
        for i in s:
            temp += int(i)
        s = str(temp)
        temp = 0
    return s

num = 138

print(addDigits(num))

# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.
def isUgly(n):
    if n <= 0:
        return False

    if n == 1:
        return True

    elif n % 2 == 0:
        return isUgly(n / 2)
    elif n % 3 == 0:
        return isUgly(n / 3)
    elif n % 5 == 0:
        return isUgly(n / 5)
    else:
        return False

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
def missingNumber(nums):

    srt = set(nums)
    check = list(range(0, len(srt) + 1))

    number = set(check).difference(srt)
    number = list(number)

    return number[0]

# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version.
# You should minimize the number of calls to the API.

def firstBadVersion(n):

    # for i in range(1, n+1):
    #     if isBadVersion(i) == True:
    #         return i

    # Fast version

    # right = n - 1
    # left = 0
    # while (left <= right):
    #     mid = left + (right - left) // 2
    #     if isBadVersion(mid) == True:
    #         right = mid - 1
    #     else:
    #         left = mid + 1
    # return left
    pass

# Given an integer array nums,
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.
def moveZeroes(nums):
    zeros = 0
    for n in nums:
        if n == 0:
            zeros += 1

    pointer = 0

    while zeros != 0:
        if nums[pointer] == 0:
            nums.pop(pointer)
            nums.append(0)
            zeros -= 1
        else:
            pointer += 1

moveZeroes([0,0,1])


# Given a pattern and a string s, find if s follows the same pattern.
def wordPattern(pattern,s ):
    words = s.split()

    if len(pattern) == len(words):
        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))
    else:
        return False

# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        if left > right:
            return False
        else:
            rng = self.nums[left:right + 1]

            res = 0
            for n in rng:
                res += n

            return res

# Given an integer n, return true if it is a power of three.
# Otherwise, return false.
def isPowerOfThree(n):

    if n == 0:
        return False
    else:
        while n % 3 == 0:
            n /= 3
        return n == 1

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.
def countBits(n):
    res = []
    for i in range(n + 1):
        bn = str(bin(i)[2:])
        cnt = 0
        for k in bn:
            if k == "1":
                cnt += 1
        res.append(cnt)
    return res

def countBitsShorter(n):
    res = []
    for i in range(n + 1):
        bn = str(bin(i)[2:])
        res.append(bn.count("1"))
    return res

# Given an integer n, return true if it is a power of four.
# Otherwise, return false.
def isPowerOfFour(n):
    if n == 0:
        return False
    else:
        while n % 4 == 0:
            n /= 4
        return n == 1

# Write a function that reverses a string.
# The input string is given as an array of characters s.
def reverseString(s):

    for w in range(len(s) // 2):
        t = s[w]
        s[w] = s[-(w + 1)]
        s[-(w + 1)] = t

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
def reverseVowels(s):
    vowels = "aeiouAEIOU"
    res = list(s)
    v = []

    for w in range(len(res)):
        if res[w] in vowels:
            v.append(res[w])
            res[w] = "vowel"

    for w in range(len(res)):
        if res[w] == "vowel":
            res[w] = v[-1]
            v.pop()

    s = ""

    for r in res:
        s += r

    return s

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
def intersection(nums1, nums2):

    res = []

    for n in nums1:
        if n in nums2 and n not in res:
            res.append(n)

    return res

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
def intersect(nums1, nums2):
    res = []
    intersectDict = {}

    for i in nums1:
        if i not in intersectDict:
            intersectDict[i] = 1
        else:
            intersectDict[i] += 1

    for i in nums2:
        if i in intersectDict and intersectDict[i] > 0:
            res.append(i)
            intersectDict[i] -= 1

    return res

# Given a positive integer num, return true if num is a perfect square or false otherwise.
#
# A perfect square is an integer that is the square of an integer.
# In other words, it is the product of some integer with itself.
def isPerfectSquare(num):
    if num ** 0.5 % 1 == 0:
        return True
    else:
        return False

# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong,
# I will tell you whether the number I picked is higher or lower than your guess.
def guess(n):
    return n

def guessNumber(n):

    while n:
        if guess(n) == -1:
            n -= 1
        elif guess(n) == 1:
            n += 1
        elif guess(n) == 0:
            return n

# Faster method
def guessNumberBinary(n):

    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res < 0:
            right = mid - 1
        elif res > 0:
            left = mid + 1


# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
def canConstruct(ransomNote, magazine):

    if len(ransomNote) > len(magazine):
        return False

    ransomNote = list(ransomNote)
    magazine = list(magazine)

    for l in magazine:
        if l in ransomNote:
            ransomNote.remove(l)

    return len(ransomNote) == 0

# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.
def firstUniqChar(s):
    for l in s:
        c = s.count(l)
        if c == 1:
            return s.index(l)
    return -1

print(firstUniqChar("leetcode"))

# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Return the letter that was added to t.
def findTheDifference(s, t):
    for l in t:
        if t.count(l) != s.count(l):
            return l

def isSubsequence(s, t):
    i = 0
    j = 0

    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1

    return len(s) == i

isSubsequence("abc", "ahbgdc")

# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
def sumOfLeftLeaves(root):
    if not root:
        return 0

    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sumOfLeftLeaves(root.right)
    else:
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)

# Given an integer num, return a string representing its hexadecimal representation.
# For negative integers, two’s complement method is used.
# All the letters in the answer string should be lowercase characters,
# and there should not be any leading zeros in the answer except for the zero itself.
# Note: You are not allowed to use any built-in library method to directly solve this problem.
def toHex(num):
    if num >= 0:
        return hex(num)[2:]
    else:
        return hex((num + (1 << 64)) % (1 << 64))[10:]

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome
# that can be built with those letters.
def longestPalindrome(s):

    letterSet = set()

    for l in s:
        if l not in letterSet:
            letterSet.add(l)
        else:
            letterSet.remove(l)

    if len(letterSet) != 0:
        return len(s) - len(letterSet) + 1
    else:
        return len(s)

# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
def fizzBuzz(n):
    res = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))

    return res

# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.
def thirdMax(nums):

    sn = set(sorted(nums))
    sn = list(sn)

    if len(sn) < 3:
        return max(sn)

    counter = 1

    while counter != 3:
        sn.remove(max(sn))
        counter += 1

    return max(sn)


# Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.
def addStrings(num1, num2):

    numDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9}

    intNum1 = 0
    intNum2 = 0

    for n in num1:
        intNum1 = intNum1 * 10 + numDict[n]
    for n in num2:
        intNum2 = intNum2 * 10 + numDict[n]

    return str(intNum1 + intNum2)

# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.
def countSegments(s):

    res = s.split()

    return len(res)

# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
import math
def arrangeCoins(n):
    res = (math.sqrt(8 * n + 1) - 1) / 2

    return int(res)


print(arrangeCoins(18))

#Given an array nums of n integers where nums[i] is in the range [1, n],
#return an array of all the integers in the range [1, n] that do not appear in nums.
def findDisappearedNumbers(nums):

        allNums = []

        for i in range(len(nums)):
            i += 1
            allNums.append(i)

        return set(allNums).difference(set(nums))

# Each child i has a greed factor g[i], which is the minimum size of a
# cookie that the child will be content with;
# and each cookie j has a size s[j]. If s[j] >= g[i],
# we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
def findContentChildren(g, s):
    g.sort()
    s.sort()

    chld = 0
    cook = 0

    while chld < len(g) and cook < len(s):
        if s[cook] >= g[chld]:
            chld += 1
        cook += 1
    return chld

# Given a string s, check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together.
def repeatedSubstringPattern(s):

    default = s

    s = s * 2

    s = s[1:-1]

    if default in s:
        return True
    else:
        return False

def hammingDistance(x, y):

    x = list(bin(x)[2:])
    y = list(bin(y)[2:])

    while len(x) != len(y):
        if len(x) <= len(y):
            x.insert(0, '0')
        else:
            y.insert(0, '0')

    print(x)
    print(y)

    count = 0

    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1

    return count

print(hammingDistance(1, 4))


# You are given row x col grid representing a map
# where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
def islandPerimeter(grid):
    res = 0
    allGrid = len(grid)
    oneRow = len(grid[0])

    for i in range(allGrid):
        for j in range(oneRow):
            res += 4 * grid[i][j]
            if i > 0:
                res -= grid[i][j] * grid[i - 1][j]
            if i < allGrid - 1:
                res -= grid[i][j] * grid[i + 1][j]
            if j > 0:
                res -= grid[i][j] * grid[i][j - 1]
            if j < oneRow - 1:
                res -= grid[i][j] * grid[i][j + 1]

    return res

# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's
# in its binary representation.
def findComplement(num):

    num = str(bin(num)[2:])
    res = ""

    for n in num:
        if n == "1":
            res += "0"
        elif n == "0":
            res += "1"

    return int(res, 2)

# We want to reformat the string s such that each group contains exactly k characters,
# except for the first group, which could be shorter than k but still must contain at least one character.
# Furthermore, there must be a dash inserted between two groups,
# and you should convert all lowercase letters to uppercase.
def licenseKeyFormatting(s, k):
    s = s.upper()

    lst = []
    for w in s:
        if w != "-":
            lst.append(w)

    lst = lst[::-1]
    res = ""
    counter = 0

    while len(lst) > 0:
        if counter < k:
            res += lst[0]
            lst.pop(0)
            counter += 1
        else:
            res += "-"
            counter = 0

    return res[::-1]

licenseKeyFormatting("5F3Z-2e-9-w", 4)

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
def findMaxConsecutiveOnes(nums):
    res = 0
    counter = 0

    while len(nums) != 0:
        if nums[0] == 1:
            counter += 1
            nums.pop(0)
        else:
            if counter >= res:
                res = counter
                counter = 0
                nums.pop(0)
            else:
                counter = 0
                nums.pop(0)

    if counter >= res:
        res = counter

    return res

def findMaxConsecutiveOnesShort(nums):
    res = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
            res = max(res, count)
        else:
            count = 0
    return res

# A web developer needs to know how to design a web page's size.
# So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page,
# whose length L and width W satisfy the following requirements:
def constructRectangle(area):
    s = []

    for n in range(area):
        n += 1
        if area % n == 0:
            s.append(n)
    if len(s) % 2 == 0:
        leftPointer = len(s) // 2 - 1
        rightPointer = len(s) // 2
    else:
        leftPointer = len(s) // 2
        rightPointer = len(s) // 2

    while s[leftPointer] * s[rightPointer] != area:

        if s[leftPointer] >= 0:
            leftPointer -= 1
        if s[rightPointer] < len(s):
            rightPointer += 1

    return [s[rightPointer], s[leftPointer]]


def constructRectangleFast(area):
    for l in range(int(area ** 0.5), 0, -1):
        if area % l == 0:
            return [area // l, l]

# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe,
# Ashe gets poisoned for a exactly duration seconds.
# More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval
# [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset,
# and the poison effect will end duration seconds after the new attack.
def findPoisonedDuration(timeSeries, duration):
    total = duration * len(timeSeries)

    for i in range(1, len(timeSeries)):
        total -= max(0, duration - (timeSeries[i] - timeSeries[i - 1]))

    return total
# The next greater element of some element x in an array is the first greater
# element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
def nextGreaterElement(nums1, nums2):
    res = []

    for n in nums1:
        temp = nums2[nums2.index(n) + 1:]

        if len(temp) != 0 and max(temp) > n:
            tempMax = []

            for t in temp:
                if t > n:
                    tempMax.append(t)

            res.append(tempMax[0])
        else:
            res.append(-1)

    return res

# Given an array of strings words, return the words that can be typed using
# letters of the alphabet on only one row of American keyboard
def findWords(words):
    first = "qwertyuiopQWERTYUIOP"
    second = "asdfghjklASDFGHJKL"
    third = "zxcvbnmZXCVBNM"

    firstRes = []
    secondRes = []
    thirdRes = []

    for w in words:
        s = set(w)

        cnt = 0
        for i in s:
            if i not in first:
                cnt += 1
        if cnt == 0:
            firstRes.append(w)
        cnt = 0
        for i in s:
            if i not in second:
                cnt += 1
        if cnt == 0:
            secondRes.append(w)
        cnt = 0
        for i in s:
            if i not in third:
                cnt += 1
        if cnt == 0:
            thirdRes.append(w)

    return firstRes + secondRes + thirdRes

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s)
# (i.e., the most frequently occurred element) in it.
def findMode(root):
    vals = {}

    def find(root, vals):
        if root.val not in vals:
            vals[root.val] = 1
        else:
            vals[root.val] += 1

        if root.left:
            find(root.left, vals)

        if root.right:
            find(root.right, vals)

    find(root, vals)

    max_value = max(vals.values())
    res = []

    for k, v in vals.items():
        if v == max_value:
            res.append(k)

    return res

# Base 7
def convertToBase7(num):
    num = list(str(num))
    rev = []

    for i in range(0, len(num)):
        rev.append(i)

    rev = rev[::-1]
    res = 0

    for r in range(len(rev)):
        res += int(num[r]) * (7 ** rev[r])
        # += 1 * 49 + 0 * 7 + 0 * 1

    return str(res)

def convertToBase7Check(num):

        if num == 0:
            return "0"

        check = True
        if num < 0:
            check = False
            num = -num

        digits = []
        res = ""

        while num:
            digits.append(int(num % 7))
            num //= 7

        for d in digits:
            res += str(d)

        if check == False:
            return "-" + res[::-1]
        else:
            return res[::-1]


def findRelativeRanks(score):

    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

    res = []
    for i in range(len(score)):
        res.append(i)

    dct = {}

    for i in range(len(score)):
        dct[score[i]] = i

    score = sorted(score)[::-1]

    for i in range(len(score)):
        if i < 3:
            res[dct[score[i]]] = medals[i]
        else:
            res[dct[score[i]]] = str(i + 1)

    return res

print(findRelativeRanks([5,4,3,2,1]))

# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
# A divisor of an integer x is an integer that can divide x evenly.
def checkPerfectNumber(num):
    res = 0
    counter = 1

    while counter != num:
        if num % counter == 0:
            res += counter
        counter += 1

    if res == num:
        return True
    else:
        return False

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
def detectCapitalUse(word):
    if word == word.upper():
        return True
    elif word == word.lower():
        return True
    elif word[0] == word.upper()[0] and word[1:] == word.lower()[1:]:
        return True
    else:
        return False

# Given two strings a and b, return the length of the longest uncommon subsequence between a and b.
# If the longest uncommon subsequence does not exist, return -1.
def findLUSlength(a, b):
    if a == b:
        return -1
    else:
        return max(len(a), len(b))

# Given the root of a Binary Search Tree (BST),
# return the minimum absolute difference between the values of any two different nodes in the tree.
def getMinimumDifference(root):
    res = []

    def go(root):
        res.append(root.val)

        if root.left:
            go(root.left)
        if root.right:
            go(root.right)

    go(root)

    res = sorted(res)
    m = res[1] - res[0]

    for i in range(1, len(res)):
        prev = res[i - 1]
        if res[i] - prev <= m:
            m = res[i] - prev

    return m

# Given a string s and an integer k, reverse the first k characters for every 2k
# characters counting from the start of the string.
def reverseStr(s, k):
    s = list(s)

    for i in range(0, len(s), 2 * k):
        s[i: i + k] = s[i: i + k][::-1]

    res = ""
    for i in s:
        res += i

    return res

# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
def checkRecord(s):
    if s.count("A") > 1:
        return False

    if "LLL" in s:
        return False

    return True

# Given a string s, reverse the order of characters in each word within a sentence while still
# preserving whitespace and initial word order.
def reverseWords(s):
    res = ""

    s = s.split()

    for i in s:
        if len(res) == 0:
            res += i[::-1]
        else:
            res += " " + i[::-1]

    return res

# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
def arrayPairSum(nums):

    res = []

    nums = sorted(nums)

    counter = 0
    while len(res) != len(nums) // 2:
        res.append([nums[counter], nums[counter + 1]])
        counter += 2

    sm = 0

    for i in res:
        sm += min(i)

    return sm

# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with
# a different size r x c keeping its original data.
def matrixReshape(mat, r,c):
    oneLine = []
    for i in mat:
        for j in i:
            oneLine.append(j)

    res = []
    temp = []

    while len(res) != r:
        if len(temp) != c and len(oneLine) != 0:
            temp.append(oneLine[0])
            oneLine.pop(0)
        else:
            res.append(temp)
            temp = []

    if len(oneLine) > 0:
        return mat
    elif len(res) != r:
        return mat

    for i in res:
        if len(i) != c:
            return mat

    return res

""" !!!!!!!!! Binary tree comparison !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the
# same structure and node values of subRoot and false otherwise.
def isSubtree(root, subRoot):

    def convert(node):
        if node:
            return "N: " + str(node.val) + " B: " + convert(node.left) + convert(node.right)
        else:
            return "None"

    return convert(subRoot) in convert(root)


# Given the integer array candyType of length n, return the maximum number of different types of candies
# she can eat if she only eats n / 2 of them.
def distributeCandies(candyType):

    limit = len(candyType) // 2

    unique = set(candyType)

    if len(unique) > limit:
        return limit
    else:
        return len(unique)

def findLHS(nums):

    if len(set(nums)) == 1:
        return 0
    else:
        res = []
        temp = []

        while len(nums) > 0:

            nums = sorted(nums)

            mx = nums[-1]

            temp.append(mx)
            nums.pop()

            for r in nums:
                if r == mx or r == mx - 1:
                    temp.append(r)

            res.append(temp)
            temp = []

        mx = 0

        for r in res:
            if len(r) > mx and len(set(r)) != 1:
                mx = len(r)

        return mx

def findLHSDict(nums):

    count = {}
    for n in nums:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1

    mx = 0

    for n in count.keys():
        if count.get(n + 1):
            mx = max(mx, count[n] + count.get(n + 1))
    return mx

# You are given an m x n matrix M initialized with all 0's and an array of operations ops,
# where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
# Count and return the number of maximum integers in the matrix after performing all the operations.
def maxCount( m, n, ops):

    col = min(i for i, _ in ops + [[m, n]])
    row = min(j for _, j in ops + [[m, n]])

    return col * row


# Given two arrays of strings list1 and list2,
# find the common strings with the least index sum.
def findRestaurant(list1, list2):

    s1 = set(list1)
    s2 = set(list2)

    common = list(s1.intersection(s2))

    sumDict = {}

    for c in common:
        sumDict[c] = list1.index(c) + list2.index(c)

    minK = sumDict[min(sumDict, key=sumDict.get)]

    res = []

    for k, v in sumDict.items():
        if v == minK:
            res.append(k)

    return res

def canPlaceFlowers(flowerbed, n):
    
    if n == 0:
        return True

    if len(flowerbed) == 1 and flowerbed[0] == 0:
        return True
    elif len(flowerbed) == 1:
        return False

    for i in range(len(flowerbed)):
        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        elif i == len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
        elif i < len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

        if n == 0:
            return n == 0

    return n == 0

# Given the root of a binary tree, construct a string consisting of parenthesis and
# integers from a binary tree with the preorder traversal way, and return it.
def tree2str(root):

    if not root:
        return ""

    left = tree2str(root.left)
    right = tree2str(root.right)

    if left == "" and right == "":
        return str(root.val)
    elif left == "":
        return str(root.val) + "()" + "(" + right + ")"
    elif right == "":
        return str(root.val) + "(" + left + ")"
    else:
        return str(root.val) + "(" + left + ")" + "(" + right + ")"

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
def maximumProduct(nums):

    if min(nums) >= 0:
        nums = sorted(nums)[::-1]
    else:
        nums = sorted(nums)

    if min(nums) >= 0:
        return nums[0] * nums[1] * nums[2]
    elif min(nums) <= 0 and max(nums) <= 0:
        return nums[-1] * nums[-2] * nums[-3]
    else:
        first = nums[0] * nums[1] * nums[-1]
        second = nums[-3] * nums[-2] * nums[-1]
        return max(first, second)

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
def findMaxAverage(nums, k):
    mx = sum(nums[0: k])

    temp = mx

    for i in range(len(nums) - k):
        temp += nums[i + k] - nums[i]
        mx = max(temp, mx)

    return mx / k
