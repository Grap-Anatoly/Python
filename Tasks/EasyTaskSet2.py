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

# You own a Goal Parser that can interpret a string command.
# The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
# The interpreted strings are then concatenated in the original order.
#
# Given the string command, return the Goal Parser's interpretation of command.
def interpret(command):

    res = []
    counter = 0
    while counter < len(command):
        if command[counter] == "G":
            res.append("G")
            counter += 1
        elif command[counter] == "(" and command[counter + 1] == ")":
            res.append("o")
            counter += 2
        elif command[counter] == "(" and command[counter + 1] == "a":
            res.append("al")
            counter += 4

    return "".join(res)

# You are given an integer n, the number of teams in a tournament that has strange rules:
#
# If the current number of teams is even, each team gets paired with another team.
# A total of n / 2 matches are played, and n / 2 teams advance to the next round.
# If the current number of teams is odd, one team randomly advances in the tournament,
# and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1
# teams advance to the next round.
# Return the number of matches played in the tournament until a winner is decided.
def numberOfMatches(n):

    res = 0

    while n > 1:
        res += n // 2
        n -= n // 2

    return res

# You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.
#
# You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes.
# Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits.
# The final digits are then grouped as follows:
#
# 2 digits: A single block of length 2.
# 3 digits: A single block of length 3.
# 4 digits: Two blocks of length 2 each.
# The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks
# of length 1 and produce at most two blocks of length 2.
#
# Return the phone number after formatting.
def reformatNumber(number):

    check = "1234567890"

    formatted = []
    for i in number:
        if i in check:
            formatted.append(i)

    res = ""
    while len(formatted) > 0:
        if len(formatted) == 4:
            res += "".join(formatted[0:2]) + "-" + "".join(formatted[2:])
            break
        if len(formatted) == 3 or len(formatted) == 2:
            res += "".join(formatted)
            break
        else:
            res += "".join(formatted[0:3]) + "-"
            formatted = formatted[3:]

    return res

# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
#
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday,
# he will put in $1 more than the day before. On every subsequent Monday,
# he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
def totalMoney(n):

    res = 0
    money = 1
    counter = 0
    week = 1

    for i in range(n):
        if counter < 7:
            counter += 1

            res += money
            money += 1
        else:
            counter = 1
            week += 1

            money = week
            res += money
            money += 1

    return res

# You are given a string s of even length. Split this string into two halves of equal lengths,
# and let a be the first half and b be the second half.
#
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
# Notice that s contains uppercase and lowercase letters.
#
# Return true if a and b are alike. Otherwise, return false.
def halvesAreAlike(s):

    vowels = "aeiouAEIOU"

    sa = list(s)[0: len(s) // 2]
    sb = list(s)[len(s) // 2:]

    va = 0
    vb = 0

    for i in range(len(sa)):
        if sa[i] in vowels:
            va += 1
        if sb[i] in vowels:
            vb += 1

    return va == vb

# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes,
# where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
#
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
# You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
#
# Return the maximum total number of units that can be put on the truck.
def maximumUnits(boxTypes, truckSize):

    boxTypes = sorted(boxTypes, key=lambda x: x[1])[::-1]

    counter = 0
    res = 0

    for i in boxTypes:
        boxes = i[0]
        while boxes > 0:
            if counter < truckSize:
                res += i[1]
                counter += 1
                boxes -= 1
            else:
                return res

    return res

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
#
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i
# and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
def largestAltitude(gain):

    res = [0]

    for i in range(len(gain)):
        res.append(res[-1] + gain[i])

    return max(res)

# There is a hidden integer array arr that consists of n non-negative integers.
#
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1].
# For example, if arr = [1,0,2,1], then encoded = [1,2,3].
#
# You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].
#
# Return the original array arr. It can be proved that the answer exists and is unique.
def decodeXOR(encoded, first):

    res = [first]
    for i in encoded:
        res.append(res[-1] ^ i)

    return res

# You are given an array rectangles where rectangles[i] = [li, wi] represents
# the ith rectangle of length li and width wi.
#
# You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example,
# if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.
#
# Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.
#
# Return the number of rectangles that can make a square with a side length of maxLen.
def countGoodRectangles(rectangles):

    res = []
    for i in rectangles:
        res.append(min(i))

    return res.count(max(res))

# You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit
# inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.
#
# Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number.
# For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number
# 10 will be put in the box number 1 + 0 = 1.
#
# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
def countBalls(lowLimit, highLimit):

    res = {}
    for i in range(lowLimit, highLimit + 1):

        temp = 0
        for j in str(i):
            temp += int(j)

        if temp in res:
            res[temp] += 1
        else:
            res[temp] = 1

    return res[max(res, key=res.get)]

# You are given an integer array nums. The unique elements of an array are the elements that
# appear exactly once in the array.
#
# Return the sum of all the unique elements of nums.
def sumOfUnique(nums):

    unique = []
    for i in nums:
        if nums.count(i) == 1:
            unique.append(i)

    return sum(unique)

# You are given a string time in the form of  hh:mm,
# where some of the digits in the string are hidden (represented by ?).
#
# The valid times are those inclusively between 00:00 and 23:59.
#
# Return the latest valid time you can get from time by replacing the hidden digits.
def maximumTime(time):

    hours = list(time[:2])
    minutes = list(time[3:])

    if hours[0] == "?" and hours[1] == "?":
        hours[0] = "2"
        hours[1] = "3"
    else:
        if hours[1] == "?" and hours[0] == "2":
            hours[1] = "3"
        elif hours[1] == "?":
            hours[1] = "9"

        if hours[0] == "?" and int(hours[1]) > 3:
            hours[0] = "1"
        elif hours[0] == "?":
            hours[0] = "2"

    if minutes[0] == "?" and minutes[1] == "?":
        minutes[0] = "5"
        minutes[1] = "9"
    else:
        if minutes[1] == "?":
            minutes[1] = "9"

        if minutes[0] == "?":
            minutes[0] = "5"

    return "".join(hours) + ":" + "".join(minutes)

# Given an array nums, return true if the array was originally sorted in non-decreasing order,
# then rotated some number of positions (including zero). Otherwise, return false.
#
# There may be duplicates in the original array.
#
# Note: An array A rotated by x positions results in an array B of the same length such that
# A[i] == B[(i+x) % A.length], where % is the modulo operation.
def check(nums):

    srt = sorted(nums)

    for i in range(len(nums)):
        temp = srt[-1]
        srt.pop()
        srt.insert(0, temp)
        if srt == nums:
            return True

    return False

# You are given a string s consisting only of the characters '0' and '1'.
# In one operation, you can change any '0' to '1' or vice versa.
#
# The string is called alternating if no two adjacent characters are equal.
# For example, the string "010" is alternating, while the string "0100" is not.
#
# Return the minimum number of operations needed to make s alternating.
def minOperations(s):

    forvard = 0
    reverse = 0

    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "1":
                forvard += 1
            if s[i] == "0":
                reverse += 1
        else:
            if s[i] == "0":
                forvard += 1
            if s[i] == "1":
                reverse += 1

    return min(forvard, reverse)

# You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
# You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
# A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.
#
# Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
# If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.
#
# The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
def nearestValidPoint(x, y, points):

    res = {}
    for i in range(len(points)):
        if x == points[i][0] or y == points[i][1]:
            res[i] = abs(x - points[i][0]) + abs(y - points[i][1])

    if len(res) != 0:
        return min(res, key=res.get)
    else:
        return -1

# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
def mergeAlternately(word1, word2):

    word1, word2 = list(word1), list(word2)
    l = max(len(word1), len(word2))

    res = []
    for i in range(l):
        if len(word1) != 0:
            res.append(word1[0])
            word1.pop(0)
        if len(word2) != 0:
            res.append(word2[0])
            word2.pop(0)

    return "".join(res)

# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color,
# and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
#
# The ith item is said to match the rule if one of the following is true:
#
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.
def countMatches(items, ruleKey, ruleValue):

    res = 0
    for i in range(len(items)):
        if ruleKey == "type" and items[i][0] == ruleValue:
            res += 1
        if ruleKey == "color" and items[i][1] == ruleValue:
            res += 1
        if ruleKey == "name" and items[i][2] == ruleValue:
            res += 1

    return res

# Given an alphanumeric string s, return the second largest numerical digit that appears in s,
# or -1 if it does not exist.
#
# An alphanumeric string is a string consisting of lowercase English letters and digits.
def secondHighest(s):

    num = "1234567890"
    res = []
    for i in s:
        if i in num and int(i) not in res:
            res.append(int(i))

    if len(res) > 1:
        return sorted(res)[::-1][1]
    else:
        return -1

# Given a binary string s without leading zeros, return true if s
# contains at most one contiguous segment of ones. Otherwise, return false.
def checkOnesSegment(s):

    if "01" in s:
        return False
    else:
        return True

# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where
# there is one center node and exactly n - 1 edges that connect the center node with every other node.
#
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between
# the nodes ui and vi. Return the center of the given star graph.
def findCenter(edges):

    for i in edges[0]:
        count = 0
        for j in edges:
            if i in j:
                count += 1
        if count == len(edges):
            return i

def findCenterViaDict(edges):

    count = {}
    for i in edges:
        for j in i:
            if j in count:
                count[j] += 1
            else:
                count[j] = 1

    m = max(count, key=count.get)

    return m

# You are given coordinates, a string that represents the coordinates of a square of the chessboard.
# Below is a chessboard for your reference.
#
# Return true if the square is white, and false if the square is black.
def squareIsWhite(coordinates):

    squares = [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5], ['f', 6], ['g', 7], ['h', 8]]
    coordinates = list(coordinates)

    for i in squares:
        if coordinates[0] == i[0]:
            coordinates[0] = i[1]

    if coordinates[0] % 2 == 0:
        if int(coordinates[1]) % 2 == 0:
            return False
        else:
            return True
    else:
        if int(coordinates[1]) % 2 == 0:
            return True
        else:
            return False

def squareIsWhiteAlt(coordinates):

    coordinates = list(coordinates)

    if coordinates[0] in ('a', 'c', 'e', 'g'):
        if coordinates[1] in ('1', '3', '5', '7'):
            return False
        else:
            return True
    else:
        if coordinates[1] in ('1', '3', '5', '7'):
            return True
        else:
            return False

# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
#
# A subarray is defined as a contiguous sequence of numbers in an array.
#
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1.
# Note that a subarray of size 1 is ascending.
def maxAscendingSum(nums):

    if len(nums) == 1:
        return nums[0]
    else:
        res = []
        s = 0
        for i in range(len(nums)):
            if i != len(nums) - 1:
                if nums[i] < nums[i + 1]:
                    s += nums[i]
                else:
                    s += nums[i]
                    res.append(s)
                    s = 0
            else:
                if nums[i] > nums[i - 1]:
                    s += nums[i]
                    res.append(s)
                else:
                    res.append(s)

        return max(res)

# You are given a string word that consists of digits and lowercase English letters.
#
# You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34".
# Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".
#
# Return the number of different integers after performing the replacement operations on word.
#
# Two integers are considered different if their decimal representations without any leading zeros are different.
def numDifferentIntegers(word):

    numbers = "1234567890"

    t = ""
    integers = []

    for i in range(len(word)):
        if word[i] in numbers:
            t += word[i]
        else:
            integers.append(t)
            t = ""

    if len(t) > 0:
        integers.append(t)

    res = []
    for i in integers:
        if i != '' and int(i) not in res:
            res.append(int(i))

    return len(res)

# You are given an integer array nums (0-indexed). In one operation, you can choose an element of the
# array and increment it by 1.
#
# For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
# Return the minimum number of operations needed to make nums strictly increasing.
#
# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
# An array of length 1 is trivially strictly increasing.
def minOperations(nums):

    res = 0
    for i in range(len(nums)):
        if i < len(nums) - 1:
            if nums[i] >= nums[i + 1]:
                while nums[i] >= nums[i + 1]:
                    nums[i + 1] = nums[i + 1] + 1
                    res += 1
        else:
            if nums[i] < nums[i - 1]:
                while nums[i] < nums[i - 1]:
                    nums[i] = nums[i] + 1
                    res += 1

    return res

# Faster ver
def minOperationsFast(nums):

    res = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            c = nums[i]
            nums[i] += (nums[i - 1] - nums[i]) + 1
            res += nums[i] - c

    return res

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each of the words consists of only uppercase and lowercase English letters (no punctuation).
#
# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s and an integer k. You want to truncate s such that it contains only the first k words.
# Return s after truncating it.
def truncateSentence(s, k):

    s = list(s.split())

    res = ""
    for i in range(0, k):
        res += s[i] + " "

    return res[:-1]

# There is a function signFunc(x) that returns:
#
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
#
# Return signFunc(product).
#
#
def arraySign(nums):

    prod = nums[0]
    for i in range(1, len(nums)):
        prod *= nums[i]

    if prod > 0:
        return 1
    elif prod < 0:
        return -1
    else:
        return 0

# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd
# indices.
#
# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
#
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
#
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
def replaceDigits(s):

    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
             'y', 'z']

    s = list(s)
    res = []
    for i in range(len(s)):
        if i % 2 != 0:
            res.append(words[words.index(s[i - 1]) + int(s[i])])
        else:
            res.append(s[i])

    return "".join(res)

# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
# or false otherwise.
def checkIfPangram(sentence):

    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z']

    sentence = sorted(set(sentence))

    if a == sentence:
        return True
    else:
        return False

# Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n
# from base 10 to base k.
#
# After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.
def sumBase(n, k):

    res = 0
    while n:
        res += n % k
        n //= k

    return res

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each word consists of lowercase and uppercase English letters.
#
# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging
# the words in the sentence.
#
# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1"
# or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
def sortSentence(s):

    s = s.split()

    pos = {}
    for i in s:
        pos[i[-1]] = i[:-1]

    res = ""
    for i in range(1, len(pos) + 1):
        res += pos[str(i)] + " "

    return res[:-1]

# Given an integer array nums (0-indexed) and two integers target and start,
# find an index i such that nums[i] == target and abs(i - start) is minimized.
# Note that abs(x) is the absolute value of x.
#
# Return abs(i - start).
#
# It is guaranteed that target exists in nums.
def getMinDistance(nums, target, start):

    res = []
    for i in range(len(nums)):
        if nums[i] == target:
            res.append(abs(i - start))

    return min(res)

# You are given a 2D integer array logs where each logs[i] = [birthi, deathi]
# indicates the birth and death years of the ith person.
#
# The population of some year x is the number of people alive during that year.
# The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1].
# Note that the person is not counted in the year that they die.
#
# Return the earliest year with the maximum population.
def maximumPopulation(logs):

    born = []
    for i in logs:
        born.append(i[0])

    population = {}
    for i in born:
        temp = 0
        for j in logs:
            if i >= j[0] and i < j[1]:
                temp += 1
        population[i] = temp

    maxCount = population[max(population, key=population.get)]

    res = []
    for k, v in population.items():
        if v == maxCount:
            res.append(k)

    return min(res)

# A string is good if there are no repeated characters.
#
# Given a string s, return the number of good substrings of length three in s.
#
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
#
# A substring is a contiguous sequence of characters in a string.
def countGoodSubstrings(s):

    s = list(s)

    sub = []
    for i in range(0, len(s) - 1):
        if i < len(s) - 2:
            sub.append(s[i:i + 3])

    res = 0
    for i in sub:
        if len(set(i)) == len(i):
            res += 1

    return res

# Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer
# than the longest contiguous segment of 0's in s, or return false otherwise.
#
# For example, in s = "110100010" the longest continuous segment of 1s has length 2,
# and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0.
# The same applies if there is no 1's.
def checkZeroOnes(s):

    s = list(s)

    if len(s) == 1:
        if s[0] == "1":
            return True
        else:
            return False

    zeros = [0]
    ones = [0]

    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                if s[i - 1] == "1":
                    ones.append(count)
                else:
                    zeros.append(count)
                count = 1

    if count > 1:
        if s[-1] == "1":
            ones.append(count)
        else:
            zeros.append(count)

    if max(ones) > max(zeros):
        return True
    else:
        return False

# You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi]
# represents an inclusive interval between starti and endi.
#
# Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges.
# Return false otherwise.
#
# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.
def isCovered(ranges, left, right):

    for i in range(left, right + 1):
        present = False
        for j in ranges:
            if j[0] <= i and i <= j[1]:
                present = True

        if present == False:
            return False

    return True

# The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2,
# etc.).
#
# The numerical value of some string of lowercase English letters s is the concatenation of the letter values of
# each letter in s, which is then converted into an integer.
#
# For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it,
# we get 21.
# You are given three strings firstWord, secondWord, and targetWord, each consisting of
# lowercase English letters 'a' through 'j' inclusive.
#
# Return true if the summation of the numerical values of firstWord and secondWord equals
# the numerical value of targetWord, or false otherwise.
def isSumEqual(firstWord, secondWord, targetWord):

    words = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10,
             "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20,
             "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    first = ""
    second = ""
    target = ""

    for i in firstWord:
        first += str(words[i])

    for i in secondWord:
        second += str(words[i])

    for i in targetWord:
        target += str(words[i])

    return int(first) + int(second) == int(target)

# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to
# target by rotating mat in 90-degree increments, or false otherwise.
def findRotation(mat, target):

    def rotateMatrix(matrix):

        rotated = []
        i = 0
        for row in matrix:
            temp = [item[i] for item in matrix]
            rotated.append(temp)
            i += 1

        return rotated[::-1]

    r = rotateMatrix(mat)

    if r == target:
        return True
    else:
        for i in range(3):
            r = rotateMatrix(r)
            if r == target:
                return True

    return False

# Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly
# one element, or false otherwise. If the array is already strictly increasing, return true.
#
# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
def canBeIncreasing(nums):

    for i in range(len(nums)):
        temp = nums.copy()
        temp.pop(i)
        if temp == sorted(set(temp)):
            return True

    return False

# You are given an array of strings words (0-indexed).
#
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string,
# and move any character from words[i] to any position in words[j].
#
# Return true if you can make every string in words equal using any number of operations, and false otherwise.
def makeEqual(words):

    l = len(words)
    s = {}

    for i in words:
        for j in i:
            if j in s:
                s[j] += 1
            else:
                s[j] = 1

    for v in s.values():
        if v % l != 0:
            return False

    return True

# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
#
# Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
import math
def countTriples(n):

    res = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                t = math.sqrt(pow(i, 2) + pow(j, 2))
                if t.is_integer() and t <= n:
                    res += 1

    return res

# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
#
# For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product
# difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
#
# Return the maximum such product difference.
def maxProductDifference(nums):
    nums = sorted(nums)

    return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] =
# nums[nums[i]] for each 0 <= i < nums.length and return it.
#
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
def buildArray(nums):
    res = []
    for i in range(len(nums)):
        res.append(nums[nums[i]])

    return res

# Given a string s, return true if s is a good string, or false otherwise.
#
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e.,
# the same frequency).
def areOccurrencesEqual(s):

    c = {}

    for i in list(s):
        if i in c:
            c[i] += 1
        else:
            c[i] = 1

    cList = []
    for v in c.values():
        cList.append(v)

    return min(cList) == max(cList)

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and
# ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.
def getConcatenationViaLoop(nums):

    ans = []

    for i in range(2):
        for j in nums:
            ans.append(j)

    return ans

def getConcatenationEasy(nums):

    return nums * 2

# You are given a string s consisting of lowercase English letters, and an integer k.
#
# First, convert s into an integer by replacing each letter with its position in the alphabet (i.e.,
# replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of
# its digits. Repeat the transform operation k times in total.
#
# For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
#
# Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
# Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
# Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described above.
def getLucky(s, k):

    words = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
             "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
             "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    numbers = ""

    def convert(number):
        n = 0
        for i in list(number):
            n += int(i)

        return str(n)

    for i in list(s):
        numbers += str(words[i])

    for i in range(k):
        numbers = convert(numbers)

    return int(numbers)

# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] -
# nums[j]| == k.
#
# The value of |x| is defined as:
#
# x if x >= 0.
# -x if x < 0.
def countKDifference(nums, k):

    res = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and abs(nums[i] - nums[j]) == k:
                res += 1

    return res


# Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
#
# nums[a] + nums[b] + nums[c] == nums[d], and
# a < b < c < d
def countQuadruplets(nums):

    res = 0
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            for k in range(j + 1, len(nums) - 1):
                for m in range(k + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == nums[m]:
                        res += 1

    return res


# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the
# index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
#
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3
# (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.
def reversePrefix(word, ch):

    word = list(word)
    if ch in word:
        pref = "".join(word[:word.index(ch) + 1][::-1])
        left = "".join(word[word.index(ch) + 1:])
        return pref + left

    else:
        return "".join(word)


# You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with
# creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.
#
# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array,
# the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array,
# and so on.
#
# Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.
def construct2DArray(original, m, n):

    if n * m != len(original):
        return []
    else:
        res = []
        counter = 0
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[counter])
                counter += 1
            res.append(temp)

        return res


# There is a programming language with only four operations and one variable X:
#
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
#
# Given an array of strings operations containing a list of operations, return the final value of X after
# performing all the operations.
def finalValueAfterOperations(operations):

    res = 0
    for i in operations:
        if i == "++X" or i == "X++":
            res += 1
        else:
            res -= 1

    return res


# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e.,
# nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
#
# Return the maximum difference. If no such i and j exists, return -1.
def maximumDifference(nums):

    diff = []
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if i < j and nums[i] < nums[j]:
                diff.append(nums[j] - nums[i])

    if len(diff) > 0:
        return max(diff)
    else:
        return -1

# You are given a string s consisting of n characters which are either 'X' or 'O'.
#
# A move is defined as selecting three consecutive characters of s and converting them to 'O'.
# Note that if a move is applied to the character 'O', it will stay the same.
#
# Return the minimum number of moves required so that all the characters of s are converted to 'O'.
def minimumMoves(s):

    res = 0
    counter = 0

    while counter < len(s):
        if s[counter] == 'O':
            counter += 1
        else:
            counter += 3
            res += 1
    return res


# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are
# present in at least two out of the three arrays. You may return the values in any order.
def twoOutOfThree(nums1, nums2, nums3):

    res = []

    temp = list(set(nums1).intersection(set(nums2)))
    res = temp

    temp = list(set(nums2).intersection(set(nums3)))
    for i in temp:
        if i not in res:
            res.append(i)

    temp = list(set(nums1).intersection(set(nums3)))
    for i in temp:
        if i not in res:
            res.append(i)

    return res

# A distinct string is a string that is present only once in an array.
#
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
# If there are fewer than k distinct strings, return an empty string "".
#
# Note that the strings are considered in the order in which they appear in the array.
def kthDistinct(arr, k):

    dist = []
    for i in arr:
        if arr.count(i) < 2:
            dist.append(i)

    if len(dist) >= k:
        return dist[k - 1]
    else:
        return ""

# A sentence is a list of tokens separated by a single space with no leading or trailing spaces.
# Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of
# lowercase English letters.
#
# For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other
# tokens such as "puppy" are words.
# Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from
# left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).
#
# Return true if so, or false otherwise.
def areNumbersAscending(s):

    s = list(s.split(" "))
    numbers = []

    for i in s:
        if i.isnumeric() == True:
            numbers.append(i)

    for i in range(1, len(numbers)):
        if int(numbers[i]) <= int(numbers[i - 1]):
            return False

    return True

# A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!',
# '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or
# more spaces ' '.
#
# A token is a valid word if all three of the following are true:
#
# It only contains lowercase letters, hyphens, and/or punctuation (no digits).
# There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab"
# and "ab-" are not valid).
# There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are
# valid, but "a!b" and "c.," are not valid).
# Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
#
# Given a string sentence, return the number of valid words in sentence.
def countValidWords(sentence):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    sentence = list(sentence.split())
    res = 0

    for i in sentence:
        valid = True
        for j in i:
            if j.isdigit():
                valid = False
                break
            if j != j.lower():
                valid = False
                break
            if j == "-":
                if i.count(j) > 1:
                    valid = False
                    break
                if i.index(j) == 0 or i.index(j) == len(i) - 1:
                    valid = False
                    break
                elif i[i.index(j) - 1] not in letters or i[i.index(j) + 1] not in letters:
                    valid = False
                    break
            if j in ("!", ".", ",") and i.index(j) != len(i) - 1:
                valid = False
                break

        if valid == True:
            res += 1

    return res


# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each
# letter from 'a' to 'z' between word1 and word2 is at most 3.
#
# Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent,
# or false otherwise.
#
# The frequency of a letter x is the number of times it occurs in the string.
def checkAlmostEquivalent(word1, word2):
    word1 = list(word1)
    word2 = list(word2)

    res = []
    for i in range(len(word1)):
        if word1[i] in word2:
            res.append(abs(word1.count(word1[i]) - word2.count(word1[i])))
        else:
            res.append(word1.count(word1[i]))

    for i in range(len(word1)):
        if word2[i] in word1:
            res.append(abs(word2.count(word2[i]) - word1.count(word2[i])))
        else:
            res.append(word2.count(word2[i]))

    if max(res) <= 3:
        return True


# Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 ==
# nums[i], or -1 if such index does not exist.
#
# x mod y denotes the remainder when x is divided by y.
def smallestEqual(nums):

    res = []
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            res.append(i)

    if len(res) > 0:
        return min(res)
    else:
        return -1

# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each
# of the two arrays.
def countWords(words1, words2):

    common = list(set(words1).intersection(set(words2)))
    res = 0

    for i in common:
        if words1.count(i) == 1 and words2.count(i) == 1:
            res += 1

    return res

# There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and
# the (n - 1)th person is at the back of the line.
#
# You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person
# would like to buy is tickets[i].
#
# Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go
# back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not
# have any tickets left to buy, the person will leave the line.
#
# Return the time taken for the person at position k (0-indexed) to finish buying tickets.
def timeRequiredToBuy(tickets, k):

    res = 0
    counter = 0
    while tickets[k] > 0:

        if counter < len(tickets):
            if tickets[counter] > 0:
                res += 1
                tickets[counter] -= 1
                counter += 1
            else:
                counter += 1
        else:
            counter = 0

    return res

# There are n houses evenly lined up on the street, and each house is beautifully painted.
# You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith
# house.
#
# Return the maximum distance between two houses with different colors.
#
# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
def maxDistance(colors):

    res = []

    for i in colors:
        for j in colors[::-1]:
            if i != j:
                e = colors[::-1].index(j)
                res.append((len(colors) - e - 1) - colors.index(i))

    return max(res)


# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k
# that has the largest sum.
#
# Return any such subsequence as an integer array of length k.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without
# changing the order of the remaining elements.
def maxSubsequence(nums, k):

    while len(nums) != k:
        nums.remove(min(nums))

    return nums

# You are given a 0-indexed integer array nums and a target element target.
#
# A target index is an index i such that nums[i] == target.
#
# Return a list of the target indices of nums after sorting nums in non-decreasing order.
# If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
def targetIndices(nums, target):

    nums = sorted(nums)
    res = []

    for i in range(len(nums)):
        if target in nums[i:]:
            if target == nums[i]:
                res.append(i)
        else:
            break

    return res


# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
#
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
#
# Return the maximum number of words that appear in a single sentence.
def mostWordsFound(sentences):

    res = []
    for i in sentences:
        res.append(len(i.split()))

    return max(res)

# There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods
# labeled from 0 to 9.
#
# You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two
# characters in rings forms a color-position pair that is used to describe each ring where:
#
# The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
# The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto
# the rod labeled 2, and a blue ring placed onto the rod labeled 1.
#
# Return the number of rods that have all three colors of rings on them.
def countPoints(rings):

    col = "BGR"
    ringsDict = {}

    for i in range(len(rings)):
        if rings[i] in col:
            if rings[i + 1] in ringsDict:
                t = ringsDict[rings[i + 1]]
                if rings[i] not in t:
                    t += rings[i]
                    ringsDict[rings[i + 1]] = t
            else:
                ringsDict[rings[i + 1]] = rings[i]

    res = 0
    for v in ringsDict.values():
        if sorted(v) == sorted(col):
            res += 1

    return res


# Given an array of strings words, return the first palindromic string in the array.
# If there is no such string, return an empty string "".
#
# A string is palindromic if it reads the same forward and backward.
def firstPalindrome(words):

    for i in words:
        if i == i[::-1]:
            return i

    return ""

# You are given a string title consisting of one or more words separated by a single space, where each word consists
# of English letters. Capitalize the string by changing the capitalization of each word such that:
#
# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.
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

# Reversing an integer means to reverse all its digits.
#
# For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
# Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if
# reversed2 equals num. Otherwise return false.
#
#
def isSameAfterReversals(num):

    initial = num
    for i in range(2):
        num = int(str(num)[::-1])

    return initial == num

# Given a string s consisting of only the characters 'a' and 'b', return true if every 'a'
# appears before every 'b' in the string. Otherwise, return false.
def checkString(s):

    return s == "".join(sorted(s))


# A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.
#
# The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than
# or equal to the minimum cost of the two candies bought.
#
# For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3,
# they can take the candy with cost 1 for free, but not the candy with cost 4.
# Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of
# buying all the candies.
def minimumCost(cost):

    cost = sorted(cost)[::-1]
    res = 0
    temp = 2

    for i in cost:
        if temp != 0:
            res += i
            temp -= 1
        else:
            temp = 2

    return res

# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
#
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
def checkValid(matrix):

    for i in range(0, len(matrix)):
        row = []
        col = []
        for j in range(0, len(matrix)):
            if (matrix[i][j]) in row:
                return False
            else:
                row.append(matrix[i][j])

            if (matrix[j][i]) in col:
                return False
            else:
                col.append(matrix[j][i])

    return True


# A string s can be partitioned into groups of size k using the following procedure:
#
# The first group consists of the first k characters of the string, the second group consists of the next k
# characters of the string, and so on. Each character can be a part of exactly one group.
# For the last group, if the string does not have k characters remaining, a character fill is used to complete the
# group.
# Note that the partition is done so that after removing the fill character from the last group (if it exists) and
# concatenating all the groups in order, the resultant string should be s.
#
# Given the string s, the size of each group k and the character fill, return a string array denoting the composition
# of every group s has been divided into, using the above procedure.
def divideString(s, k, fill):

    res = []
    temp = ""

    for i in list(s):
        if len(temp) < k:
            temp += i
        else:
            res.append(temp)
            temp = i

    while len(temp) < k:
        temp += fill
    else:
        res.append(temp)

    return res

# You are given a positive integer num consisting of exactly four digits. Split num into two new
# integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2,
# and all the digits found in num must be used.
#
# For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs
# [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
# Return the minimum possible sum of new1 and new2.
def minimumSum(num):

    num = sorted(list(str(num)))
    pair1 = int(num[0] + num[3])
    pair2 = int(num[1] + num[2])

    return pair1 + pair2

# Given an integer array nums, return the number of elements that have both a strictly smaller and
# a strictly greater element appear in nums.
def countElements(nums):
    elem = []
    numsUnique = sorted(set(nums))

    for i in range(1, len(numsUnique) - 1):
        if numsUnique[i - 1] < numsUnique[i] and numsUnique[i + 1] > numsUnique[i]:
            elem.append(numsUnique[i])

    res = 0
    for i in elem:
        res += nums.count(i)

    return res

# You are given an array of integers nums. You are also given an integer original which is the first number
# that needs to be searched for in nums.
#
# You then do the following steps:
#
# If original is found in nums, multiply it by two (i.e., set original = 2 * original).
# Otherwise, stop the process.
# Repeat this process with the new number as long as you keep finding the number.
# Return the final value of original.
def findFinalValue(nums, original):

    while original in nums:
        original *= 2

    return original

# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where
# 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
#
def countPairs(nums, k):

    res = 0
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if 0 <= i < j < len(nums):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1

    return res

# You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:
#
# Sort the values at odd indices of nums in non-increasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3
# are sorted in non-increasing order.

# Sort the values at even indices of nums in non-decreasing order.
# For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2
# are sorted in non-decreasing order.
# Return the array formed after rearranging the values of nums.
def sortEvenOdd(nums):

    odd = []
    even = []
    for i in range(len(nums)):
        if i % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])

    even = sorted(even)
    odd = sorted(odd)[::-1]

    res = []
    for i in range(len(nums)):
        if i % 2 == 0:
            res.append(even[0])
            even.pop(0)
        else:
            res.append(odd[0])
            odd.pop(0)

    return res

# You are given two non-negative integers num1 and num2.
#
# In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.
#
# For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4.
# However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
# Return the number of operations required to make either num1 = 0 or num2 = 0.
def countOperations(num1, num2):

    res = 0
    while True:
        if num1 == 0 or num2 == 0:
            return res
        else:
            if num1 >= num2:
                num1 -= num2
                res += 1
            else:
                num2 -= num1
                res += 1

# You are given an array of strings words and a string pref.
#
# Return the number of strings in words that contain pref as a prefix.
#
# A prefix of a string s is any leading contiguous substring of s.
def prefixCount(words, pref):

    res = 0
    for i in words:
        if i[0:len(pref)] == pref:
            res += 1

    return res

# Given a positive integer num, return the number of positive integers less
# than or equal to num whose digit sums are even.
#
# The digit sum of a positive integer is the sum of all its digits.
def countEven(num):

    res = 0
    for i in range(1, num + 1):
        sm = 0
        for j in str(i):
            sm += int(j)
        if sm % 2 == 0:
            res += 1

    return res

# A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
#
# <col> denotes the column number c of the cell. It is represented by alphabetical letters.
# For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
# <row> is the row number r of the cell. The rth row is represented by the integer r.
# You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1,
# <row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2,
# such that r1 <= r2 and c1 <= c2.
#
# Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2.
# The cells should be represented as strings in the format mentioned above and be sorted in non-decreasing order first
# by columns and then by rows.
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

# You are given an integer array nums consisting of 2 * n integers.
#
# You need to divide nums into n pairs such that:
#
# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.
def divideArray(nums):

    for i in set(nums):
        if nums.count(i) % 2 != 0:
            return False

    return True

# You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.
#
# For every unique integer target in nums, count the number of times target immediately follows an occurrence of
# key in nums. In other words, count the number of indices i such that:
#
# 0 <= i <= nums.length - 2,
# nums[i] == key and,
# nums[i + 1] == target.
# Return the target with the maximum count. The test cases will be generated such that the target with maximum
# count is unique.
def mostFrequent(nums, key):

    c = Counter()
    for i, n in enumerate(nums):
        if n == key and i + 1 < len(nums):
            c[nums[i + 1]] += 1

    return c.most_common(1)[0][0]

# You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the
# closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a
# valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of
# the same hill or valley if nums[i] == nums[j].
#
# Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on
# both the left and right of the index.
#
# Return the number of hills and valleys in nums.
#
#
def countHillValley(nums):

    n = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            n.append(nums[i])
    nums = n

    res = 0
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
            res += 1
        elif nums[i] < nums[i - 1] and nums[i + 1] > nums[i]:
            res += 1
    return res

# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for
# which there exists at least one index j such that |i - j| <= k and nums[j] == key.
#
# Return a list of all k-distant indices sorted in increasing order.
def findKDistantIndices(nums, key, k):

    res = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if abs(i - j) <= k and nums[j] == key:
                res.append(i)

    return list(set(res))


# A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1
# to 0.
#
# For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not
# shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get
# 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
# Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
def minBitFlips(start, goal):

    xor = start ^ goal
    res = 0

    while xor:
        xor &= xor - 1
        res += 1

    return res

# You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e.
# both odd digits or both even digits).
#
# Return the largest possible value of num after any number of swaps.
def largestInteger(num):

    odd = []
    even = []
    orig = []
    for i in str(num):
        if int(i) % 2 == 0:
            even.append(i)
            orig.append("even")
        else:
            odd.append(i)
            orig.append("odd")

    odd = sorted(odd)[::-1]
    even = sorted(even)[::-1]

    res = []
    for i in orig:
        if i == "even":
            res.append(even[0])
            even.pop(0)
        else:
            res.append(odd[0])
            odd.pop(0)

    return int("".join(res))

# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of
# integers that are present in each array of nums sorted in ascending order.
def intersection(nums):

    n = nums[0]
    for i in nums:
        if len(i) > len(n):
            n = i

    res = []
    for i in n:
        count = 0
        for j in nums:
            if i in j:
                count += 1

        if count == len(nums):
            res.append(i)
        else:
            count = 0

    return sorted(res)

# You are given a string number representing a positive integer and a character digit.
#
# Return the resulting string after removing exactly one occurrence of digit from number such that the value of the
# resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least
# once in number.
def removeDigit(number, digit):

    mx = 0
    number = list(number)
    for i in range(len(number)):
        if number[i] == digit:
            number[i] = ""
            if int("".join(number)) > mx:
                mx = int("".join(number))
            number[i] = digit

    return str(mx)

# You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.
#
# Return the number of strings in words that are a prefix of s.
#
# A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence
# of characters within a string.
def countPrefixes(words, s):

    res = 0
    for i in words:
        if i in s[0:len(i)]:
            res += 1

    return res

# You are given a string num representing a large integer. An integer is good if it meets the following conditions:
#
# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.
#
# Note:
#
# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.
#  
def largestGoodInteger(num):

    res = []
    for i in range(len(list(num)) - 2):
        if num[i] == num[i + 1] and num[i] == num[i + 2]:
            res.append(num[i] * 3)

    if len(res) > 0:
        return sorted(res)[-1]
    else:
        return ""

# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers, return the number with the largest value.
def findClosestNumber(nums):

    lower = []
    bigger = []
    for i in nums:
        if i < 0:
            lower.append(i)
        else:
            bigger.append(i)

    if len(lower) > 0 and len(bigger) > 0:
        if abs(sorted(lower)[-1]) < sorted(bigger)[0]:
            return sorted(lower)[-1]
        else:
            return sorted(bigger)[0]
    elif len(lower) == 0:
        return sorted(bigger)[0]
    else:
        return sorted(lower)[-1]

# You are given a string s consisting of digits and an integer k.
#
# A round can be completed if the length of s is greater than k. In one round, do the following:
#
# Divide s into consecutive groups of size k such that the first k characters are in the first group,
# the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k.
# Replace each group of s with a string representing the sum of all its digits. For example, "346" is
# replaced with "13" because 3 + 4 + 6 = 13.
# Merge consecutive groups together to form a new string. If the length of the string is greater than k,
# repeat from step 1.
# Return s after all rounds have been completed.
def digitSum(s, k):

    s = list(s)

    def splitIntoKChunks(s, k):
        res = []
        temp = []

        for i in range(len(s)):
            if len(temp) < k:
                temp.append(s[i])
            else:
                res.append("".join(temp))
                temp = [s[i]]

        if len(temp) != 0:
            res.append("".join(temp))

        return res

    while len(s) > k:
        r = splitIntoKChunks(s, k)
        s = ""
        for i in r:
            t = 0
            for v in i:
                t += int(v)
            s += str(t)

    return "".join(s)

# Given a string s and a character letter, return the percentage of characters in s that equal letter
# rounded down to the nearest whole percent.
def percentageLetter(s, letter):

    c = s.count(letter)

    return int(c / len(s) * 100)

# You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new
# strings.
#
# Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.
def rearrangeCharacters(s, target):

    def countOccurances(string):
        res = {}
        for i in string:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        return res

    sCount = countOccurances(s)
    tCount = countOccurances(target)

    res = []
    for k, v in tCount.items():
        if k in sCount.keys():
            res.append(sCount[k] // tCount[k])
        else:
            return 0

    return min(res)

# You are given a 0-indexed string num of length n consisting of digits.
#
# Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise
# return false.
def digitCount(num):
    for i in range(len(num)):
        if num.count(str(i)) != int(num[i]):
            return False

    return True

# Given two integers num1 and num2, return the sum of the two integers.
def sum(self, num1, num2):

    return num1 + num2

# You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
#
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.
def checkTree(root):
    return root.val == root.left.val + root.right.val

# You are given a 0-indexed integer array nums whose length is a power of 2.
#
# Apply the following algorithm on nums:
#
# Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of
# length n / 2.
# For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
# For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.
# Return the last number that remains in nums after applying the algorithm.
def minMaxGame(nums):

    while len(nums) != 1:
        newNums = []
        for i in range(len(nums) // 2):
            if i % 2 == 0:
                newNums.append(min(nums[2 * i], nums[2 * i + 1]))
            else:
                newNums.append(max(nums[2 * i], nums[2 * i + 1]))
        nums = newNums

    return nums[0]

# A password is said to be strong if it satisfies all the following criteria:
#
# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
# Given a string password, return true if it is a strong password. Otherwise, return false.
def strongPasswordCheckerII(password):

    if len(password) < 8:
        return False

    if password == password.upper():
        return False

    if password == password.lower():
        return False

    digit = False
    for i in "1234567890":
        if i in password:
            digit = True
            break

    if digit == False:
        return False

    special = False
    for i in "!@#$%^&*()-+":
        if i in password:
            special = True
            break

    if special == False:
        return False

    password = list(password)
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return False

    return True

# A square matrix is said to be an X-Matrix if both of the following conditions hold:
#
# All the elements in the diagonals of the matrix are non-zero.
# All other elements are 0.
# Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.
def checkXMatrix(grid):

    xMatrix = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == j or i == len(grid) - 1 - j:
                if grid[i][j] == 0:
                    xMatrix = False
            else:
                if grid[i][j] != 0:
                    xMatrix = False

    return xMatrix == True

# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
# In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
#
# Return the number of '*' in s, excluding the '*' between each pair of '|'.
#
# Note that each '|' will belong to exactly one pair.
def countAsterisks(s):

    s = list(s.split("|"))
    res = 0

    for i in range(len(s)):
        if i % 2 == 0:
            res += s[i].count("*")

    return res

# You are given the strings key and message, which represent a cipher key and a secret message, respectively.
# The steps to decode message are as follows:
#
# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
# we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.
def decodeMessage(key, message):

        letters = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k",
                   12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u",
                   22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}

        code = {}
        clean = []
        key = list(key)

        for i in key:
            if i not in clean:
                clean.append(i)

        pointer = 1
        for i in range(len(clean)):
            if clean[i] != ' ':
                code[clean[i]] = pointer
                pointer += 1

        res = []
        for i in list(message):
            if i != " ":
                res.append(letters[code[i]])
            else:
                res.append(' ')

        return "".join(res)