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

# You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up
# 2 cups with different types of water, or 1 cup of any type of water.
#
# You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the
# number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed
# to fill up all the cups.
def fillCups(amount):
    res = 0
    while amount != [0, 0, 0]:
        amount = sorted(amount)[::-1]
        if amount[1] > 0:
            amount[0] -= 1
            amount[1] -= 1
            res += 1
        else:
            amount[0] -= 1
            res += 1

    return res

# You are given the root of a full binary tree with the following properties:
#
# Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
# Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
# The evaluation of a node is as follows:
#
# If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
# Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's
# evaluations.
# Return the boolean result of evaluating the root node.
#
# A full binary tree is a binary tree where each node has either 0 or 2 children.
#
# A leaf node is a node that has zero children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def evaluateTree(root):
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return root.val

    if root.val == 2:
        return evaluateTree(root.left) or evaluateTree(root.right)
    else:
        return evaluateTree(root.left) and evaluateTree(root.right)

# You are given a 0-indexed integer array nums. In one operation, you may do the following:
#
# Choose two integers in nums that are equal.
# Remove both integers from nums, forming a pair.
# The operation is done on nums as many times as possible.
#
# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and
# answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.
def numberOfPairs(nums):

    res = [0, 0]

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] == nums[j] and nums[i] != "":
                    res[0] = res[0] + 1
                    nums[i] = ""
                    nums[j] = ""

    for i in nums:
        if i != "":
            res[1] += 1

    return res

# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
#
# Note:
#
# A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# s will contain at least one letter that appears twice.
def repeatedCharacter(s):

    temp = []
    for i in s:
        if i in temp:
            return i
        else:
            temp.append(i)

# You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a
# rank of ranks[i] and a suit of suits[i].
#
# The following are the types of poker hands you can make from best to worst:
#
# "Flush": Five cards of the same suit.
# "Three of a Kind": Three cards of the same rank.
# "Pair": Two cards of the same rank.
# "High Card": Any single card.
# Return a string representing the best type of poker hand you can make with the given cards.
#
# Note that the return values are case-sensitive.
def bestHand(self, ranks: List[int], suits: List[str]) -> str:

    res = {"Flush": 0, "Three of a Kind": 0, "Pair": 0, "High Card": 0}

    if len(set(suits)) == 1:
        res['Flush'] = 1
    for i in set(ranks):
        if ranks.count(i) >= 3:
            res['Three of a Kind'] = 1
        if ranks.count(i) == 2:
            res['Pair'] = 1
    else:
        res['High Card'] = 1

    for k, v in res.items():
        if v == 1:
            return k

# You are given a non-negative integer array nums. In one operation, you must:
#
# Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
# Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.
def minimumOperations(nums):
    res = 0
    for i in nums:
        if set(nums) != 0:
            if i != 0:
                for j in range(len(nums)):
                    if i == nums[j]:
                        nums[j] = 0
                res += 1

    return res

# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k)
# is an arithmetic triplet if the following conditions are met:
#
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.
def arithmeticTriplets(nums, diff):

    res = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i < j < k:
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        res += 1

    return res

# You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the
# following properties:
#
# items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
# The value of each item in items is unique.
# Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all
# items with value valuei.
#
# Note: ret should be returned in ascending order by value.
def mergeSimilarItems(items1, items2):

    res = {}
    for i in items1:
        if i[0] not in res:
            res[i[0]] = i[1]
        else:
            res[i[0]] += i[1]
    for i in items2:
        if i[0] not in res:
            res[i[0]] = i[1]
        else:
            res[i[0]] += i[1]

    resList = []
    for k, v in res.items():
        resList.append([k, v])

    return sorted(resList)

# You are given an n x n integer matrix grid.
#
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
#
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
#
# Return the generated matrix.
def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

    res = [[1] * (len(grid) - 2) for i in range(len(grid) - 2)]
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            res[i - 1][j - 1] = max(grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1], grid[i][j - 1],
                                    grid[i][j], grid[i][j + 1], grid[i + 1][j - 1], grid[i + 1][j],
                                    grid[i + 1][j + 1])

    return res

# You are entering a competition, and are given two positive integers initialEnergy and initialExperience denoting
# your initial energy and initial experience respectively.
#
# You are also given two 0-indexed integer arrays energy and experience, both of length n.
#
# You will face n opponents in order. The energy and experience of the ith opponent is denoted by energy[i] and
# experience[i] respectively. When you face an opponent, you need to have both strictly greater experience and energy
# to defeat them and move to the next opponent if available.
#
# Defeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i].
#
# Before starting the competition, you can train for some number of hours. After each hour of training, you can either
# choose to increase your initial experience by one, or increase your initial energy by one.
#
# Return the minimum number of training hours required to defeat all n opponents.
def minNumberOfHours(initialEnergy, initialExperience, energy, experience):

    res = 0
    opponents = 0

    while opponents < len(energy):
        if initialExperience > experience[opponents] and initialEnergy > energy[opponents]:
            initialEnergy -= energy[opponents]
            initialExperience += experience[opponents]
            opponents += 1
        else:
            while initialEnergy <= energy[opponents]:
                initialEnergy += 1
                res += 1
            while initialExperience <= experience[opponents]:
                initialExperience += 1
                res += 1

            if initialExperience > experience[opponents] and initialEnergy > energy[opponents]:
                initialEnergy -= energy[opponents]
                initialExperience += experience[opponents]
                opponents += 1

    return res

# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of
# the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
#
# You are also given an integer k, which is the desired number of consecutive black blocks.
#
# In one operation, you can recolor a white block such that it becomes a black block.
#
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black
# blocks.
def minimumRecolors(blocks, k):
    if "B" * k in blocks:
        return 0
    else:
        blocks = list(blocks)
        res = []

        for i in range(len(blocks) - k + 1):
            res.append(blocks[i:i + k].count("W"))

        return min(res)

# You are given an integer array nums of length n, and an integer array queries of length m.
#
# Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums
# such that the sum of its elements is less than or equal to queries[i].
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing
# the order of the remaining elements.
#
#
def answerQueries(nums, queries):

    nums = sorted(nums)
    res = []
    for i in queries:
        sm = 0
        size = 0
        for j in range(len(nums)):
            if sm + nums[j] <= i:
                sm += nums[j]
                size += 1
        res.append(size)

    return res

# Easy
# Topics
# Companies
# Hint
# You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears
# exactly twice. You are also given a 0-indexed integer array distance of length 26.
#
# Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
#
# In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If
# the ith letter does not appear in s, then distance[i] can be ignored.
#
# Return true if s is a well-spaced string, otherwise return false.
def checkDistances(s, distance):

    s = list(s)
    letters = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
               "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
               "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    for i in range(len(s)):
        dist = 0
        for j in range(i + 1, len(s)):
            if s[j] != s[i]:
                dist += 1
            else:
                if distance[letters[s[i]] - 1] != dist:
                    return False

    return True

# Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum.
# Note that the two subarrays must begin at different indices.
#
# Return true if these subarrays exist, and false otherwise.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
def findSubarrays(nums):

    res = {}
    for i in range(len(nums) - 1):
        sm = sum(nums[i:i + 2])
        if sm in res:
            return True
        else:
            res[sm] = sm
    return False

# Given an integer array nums, return the most frequent even element.
#
# If there is a tie, return the smallest one. If there is no such element, return -1
def mostFrequentEven(nums):

    even = {}
    for i in nums:
        if i % 2 == 0:
            even[i] = nums.count(i)

    res = []
    if len(even) > 0:
        m = even[max(even, key=even.get)]
        for k, v in even.items():
            if v == m:
                res.append(k)

        return min(res)
    else:
        return -1

# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
def smallestEvenMultiple(n):

    if n % 2 == 0:
        return n
    else:
        return n * 2

# Alice and Bob are traveling to Rome for separate business meetings.
#
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates
# arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob
# (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
#
# Return the total number of days that Alice and Bob are in Rome together.
#
# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days
# per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

    res = 0
    res = max(0, self.getDate(min(leaveAlice, leaveBob)) - self.getDate(max(arriveAlice, arriveBob)) + 1)

    return res

def getDate(self, date):
    monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = int(date[:2])
    days = int(date[3:])
    return sum(monthList[: month - 1]) + days

# You are given an array of strings names, and an array heights that consists of distinct positive integers.
# Both arrays are of length n.
#
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
#
# Return names sorted in descending order by the people's heights.
def sortPeople(names, heights):

    heightsSet = []
    for i in range(len(names)):
        heightsSet.append([heights[i], names[i]])

    res = []
    for i in sorted(heightsSet)[::-1]:
        res.append(i[1])

    return res

# Given two positive integers a and b, return the number of common factors of a and b.
#
# An integer x is a common factor of a and b if x divides both a and b.
def commonFactors(a, b):

    res = 0
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            res += 1

    return res

# There are n employees, each with a unique id from 0 to n - 1.
#
# You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:
#
# idi is the id of the employee that worked on the ith task, and
# leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.
# Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.
#
# Return the id of the employee that worked the task with the longest time. If there is a tie between two or more
# employees, return the smallest id among them.
def hardestWorker(n, logs):

    res = []
    for i in range(len(logs)):
        if i == 0:
            res.append(logs[i][::-1])
        else:
            res.append([logs[i][1] - logs[i - 1][1], logs[i][0]])

    ids = []
    mx = sorted(res)[::-1][0]
    for i in sorted(res)[::-1]:
        if i[0] == mx[0]:
            ids.append(i[1])

    return min(ids)

# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k
# also exists in the array.
#
# Return the positive integer k. If there is no such integer, return -1.
def findMaxK(nums):

    res = []
    for i in nums:
        if i > 0 and (i * -1) in nums:
            res.append(i)

    if len(res) > 0:
        return max(res)
    else:
        return -1

# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and
# remove the letter at that index from word so that the frequency of every letter present in word is equal.
#
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal,
# and false otherwise.
#
# Note:
#
# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.
def equalFrequency(word):

    word = list(word)
    temp = []
    check = False

    for i in range(len(word)):
        temp = word[:i] + word[i + 1:]
        check = True

        f = temp.count(temp[0])
        for i in temp:
            if temp.count(i) != f:
                check = False

        if check == True:
            return True

    return False

# You are given two arrays of strings that represent two inclusive events that happened on the same day,
# event1 and event2, where:
#
# event1 = [startTime1, endTime1] and
# event2 = [startTime2, endTime2].
# Event times are valid 24 hours format in the form of HH:MM.
#
# A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).
#
# Return true if there is a conflict between two events. Otherwise, return false.
def haveConflict(event1, event2):

    event1Start, event1End = event1
    event2Start, event2End = event2

    if event2End < event1Start:
        return False
    if event2Start > event1End:
        return False

    return True

# Given an integer array nums of positive integers, return the average value of all even integers that are divisible
# by 3.
#
# Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
def averageValue(nums):

    res = []
    for i in nums:
        if i % 3 == 0 and i % 2 == 0:
            res.append(i)

    if len(res) > 0:
        return sum(res) // len(res)
    else:
        return 0

# You are given an array of equal-length strings words. Assume that the length of each string is n.
#
# Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 where
# difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference between two
# letters is the difference between their positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and
# 'z' is 25.
#
# For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
# All the strings in words have the same difference integer array, except one. You should find that string.
#
# Return the string in words that has different difference integer array.
def oddString(words):
    n = len(words)
    m = len(words[0])
    diff = []
    for i in range(n):
        subList = []
        for j in range(m - 1):
            subList.append(ord(words[i][j + 1]) - ord(words[i][j]))
        diff.append(tuple(subList))

    for i in range(n):
        if collections.Counter(diff)[diff[i]] == 1:
            return words[i]

# You are given a 0-indexed array nums of size n consisting of non-negative integers.
#
# You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the
# following on the ith element of nums:
#
# If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
# After performing all the operations, shift all the 0's to the end of the array.
#
# For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
# Return the resulting array.
#
# Note that the operations are applied sequentially, not all at once.
def applyOperations(nums):

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    res = []
    for i in nums:
        if i != 0:
            res.append(i)

    while len(res) != len(nums):
        res.append(0)

    return res

# You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the
# temperature in Celsius.
#
# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
#
# Return the array ans. Answers within 10-5 of the actual answer will be accepted.
#
# Note that:
#
# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00
def convertTemperature(celsius):

    return [celsius + 273.15, celsius * 1.80 + 32.00]

# You are given a 0-indexed integer array nums of even length.
#
# As long as nums is not empty, you must repetitively:
#
# Find the minimum number in nums and remove it.
# Find the maximum number in nums and remove it.
# Calculate the average of the two removed numbers.
# The average of two numbers a and b is (a + b) / 2.
#
# For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
# Return the number of distinct averages calculated using the above process.
def distinctAverages(nums):
    res = []
    nums = sorted(nums)

    while len(nums) != 0:
        res.append((nums[0] + nums[-1]) / 2)
        nums.pop(0)
        nums.pop(-1)

    return len(set(res))

# You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the
# following conditions:
#
# 0 <= i < j < k < nums.length
# nums[i], nums[j], and nums[k] are pairwise distinct.
# In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
# Return the number of triplets that meet the conditions.
def unequalTriplets(nums):

    res = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] != nums[j] and nums[j] != nums[k] and nums[k] != nums[i]:
                    res += 1

    return res

# Given a positive integer n, find the pivot integer x such that:
#
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most
# one pivot index for the given input.
#
#
def pivotInteger(n):

    for i in range(1, n + 1):

        if sum(range(1, i + 1)) == sum(range(i, n + 1)):
            return i

    return -1

# A valid cut in a circle can be:
#
# A cut that is represented by a straight line that touches two points on the edge of the circle and passes through
# its center, or
# A cut that is represented by a straight line that touches one point on the edge of the circle and its center.
# Some valid and invalid cuts are shown in the figures below.
def numberOfCuts(n):
    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            return n // 2
        else:
            return n

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
#
# For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are
# considered different.
#
# A sentence is circular if:
#
# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.
# For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences.
# However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.
#
# Given a string sentence, return true if it is circular. Otherwise, return false.
def isCircularSentence(sentence):
    sentence = sentence.split()
    if len(sentence) == 1:
        return sentence[0][0] == sentence[0][-1]
    else:
        for i in range(len(sentence)):
            if i != len(sentence) - 1:
                if sentence[i][-1] != sentence[i + 1][0]:
                    return False
            else:
                if sentence[i][-1] != sentence[0][0]:
                    return False

        return True

# You are given an m x n matrix grid consisting of positive integers.
#
# Perform the following operation until grid becomes empty:
#
# Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
# Add the maximum of deleted elements to the answer.
# Note that the number of columns decreases by one after each operation.
#
# Return the answer after performing the operations described above.
def deleteGreatestValue(grid):

    for i in range(len(grid)):
        grid[i] = sorted(grid[i])[::-1]

    res = []
    for i in range(len(grid[0])):
        temp = []
        for j in range(len(grid)):
            temp.append(grid[j][0])
            grid[j].pop(0)
        res.append(max(temp))

    return sum(res)

# The value of an alphanumeric string can be defined as:
#
# The numeric representation of the string in base 10, if it comprises of digits only.
# The length of the string, otherwise.
# Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
def maximumValue(strs):

    numbers = '1234567890'
    res = []
    for i in strs:
        number = True
        for j in i:
            if j not in numbers:
                number = False

        if number == True:
            res.append(int(i))
        else:
            res.append(len(i))

    return max(res)

# You are given a 0-indexed string array words.
#
# Two strings are similar if they consist of the same characters.
#
# For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
# However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
# Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i]
# and words[j] are similar.
def similarPairs(words):

    res = 0
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and set(words[i]) == set(words[j]):
                res += 1

    return res // 2

# You are given a 0-indexed circular string array words and a string target. A circular array means that the
# array's end connects to the array's beginning.
#
# Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words
# [(i - 1 + n) % n], where n is the length of words.
# Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.
#
# Return the shortest distance needed to reach the string target. If the string target does not exist in words,
# return -1.
def closetTarget(words, target, startIndex):

    if target in words:
        right = 0
        left = 0

        lp, rp = startIndex, startIndex

        for i in range(len(words)):
            if rp >= len(words):
                rp = 0
            if words[rp] != target:
                rp += 1
                right += 1

        for i in range(len(words)):
            if words[lp] != target:
                lp -= 1
                left += 1

        return min(right, left)
    else:
        return -1

# You are given a 0-indexed integer array forts of length n representing the positions of several forts.
# forts[i] can be -1, 0, or 1 where:
#
# -1 represents there is no fort at the ith position.
# 0 indicates there is an enemy fort at the ith position.
# 1 indicates the fort at the ith the position is under your command.
# Now you have decided to move your army from one of your forts at position i to an empty position j such that:
#
# 0 <= i, j <= n - 1
# The army travels over enemy forts only. Formally, for all k where min(i,j) < k < max(i,j), forts[k] == 0.
# While moving the army, all the enemy forts that come in the way are captured.
#
# Return the maximum number of enemy forts that can be captured. In case it is impossible to move your army,
# or you do not have any fort under your command, return 0.
def captureForts(forts):

    res = []
    i = 0
    while i < len(forts):
        if forts[i] == 1 and i != len(forts) - 1:
            pointer = 0
            i += 1
            while forts[i] == 0 and i != len(forts) - 1:
                pointer += 1
                i += 1
            if forts[i] == -1:
                res.append(pointer)
        else:
            i += 1

    i = len(forts) - 1
    while i > 0:
        if forts[i] == 1 and i != 0:
            pointer = 0
            i -= 1
            while forts[i] == 0:
                pointer += 1
                i -= 1
            if i >= 0 and forts[i] == -1:
                res.append(pointer)
        else:
            i -= 1

    if len(res) > 0:
        return max(res)
    else:
        return 0

# Given an integer num, return the number of digits in num that divide num.
#
# An integer val divides nums if nums % val == 0.
def countDigits(num):

    res = 0
    for i in str(num):
        if num % int(i) == 0:
            res += 1

    return res

# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive
# integers and the number of negative integers.
#
# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg,
# then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.
def maximumCount(nums):

    res = [0, 0]
    for i in nums:
        if i < 0:
            res[0] += 1
        elif i > 0:
            res[1] += 1

    return max(res)

# Given four integers length, width, height, and mass, representing the dimensions and mass of a box,
# respectively, return a string representing the category of the box.
#
# The box is "Bulky" if:
# Any of the dimensions of the box is greater or equal to 104.
# Or, the volume of the box is greater or equal to 109.
# If the mass of the box is greater or equal to 100, it is "Heavy".
# If the box is both "Bulky" and "Heavy", then its category is "Both".
# If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
# If the box is "Bulky" but not "Heavy", then its category is "Bulky".
# If the box is "Heavy" but not "Bulky", then its category is "Heavy".
# Note that the volume of the box is the product of its length, width and height.
def categorizeBox(length, width, height, mass):

    res = []
    if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or length * width * height >= 10 ** 9:
        res.append("Bulky")
    if mass >= 100:
        res.append("Heavy")

    if "Bulky" in res and "Heavy" in res:
        return "Both"

    if "Bulky" not in res and "Heavy" not in res:
        return "Neither"

    return res[0]

# You are given a positive integer array nums.
#
# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.
#
# Note that the absolute difference between two integers x and y is defined as |x - y|.
def differenceOfSum(nums):

    res = [0, 0]
    for i in nums:
        res[0] += i
        for j in str(i):
            res[1] += int(j)

    return abs(res[0] - res[1])

# You are given a positive integer n. Each digit of n has a sign according to the following rules:
#
# The most significant digit is assigned a positive sign.
# Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.
def alternateDigitSum(n):

    res = 0
    for i in range(len(str(n))):
        if i % 2 == 0:
            res += int(str(n)[i])
        else:
            res -= int(str(n)[i])

    return res

# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to
# both arrays. If there is no common integer amongst nums1 and nums2, return -1.
#
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that
# integer.
def getCommon(nums1, nums2):

    сommon = []
    common = list(set(nums1).intersection(set(nums2)))

    if len(common) > 0:
        return min(common)
    else:
        return -1

# Given an array of positive integers nums, return an array answer that consists of the digits of each integer
# in nums after separating them in the same order they appear in nums.
#
# To separate the digits of an integer is to get all the digits it has in the same order.
#
# For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
def separateDigits(nums):

    res = []
    for i in nums:
        if len(str(i)) > 1:
            for j in str(i):
                res.append(int(j))
        else:
            res.append(i)

    return res

# There are n people standing in a line labeled from 1 to n. The first person in the line is holding a
# pillow initially. Every second, the person holding the pillow passes it to the next person standing in
# the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing
# the pillow in the opposite direction.
#
# For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n -
# 2th person and so on.
# Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.
def passThePillow(n, time):

    counter = 1
    direction = "left"
    for i in range(time):
        action = 1

        if direction == "left" and counter < n and action > 0:
            counter += 1

            action = 0

        if direction == "left" and counter == n and action > 0:
            direction = "right"
            counter -= 1

            action = 0

        if direction == "right" and counter > 1 and action > 0:
            counter -= 1

            action = 0

        if direction == "right" and counter == 1 and action > 0:
            direction = "left"
            counter += 1

            action = 0

    return counter

# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
#
# The concatenation of num1 and num2 is a permutation of num.
# In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number
# of occurrences of that digit in num.
# num1 and num2 can contain leading zeros.
# Return the minimum possible sum of num1 and num2.
#
# Notes:
#
# It is guaranteed that num does not contain any leading zeros.
# The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.
def splitNum(num):

        num = list(str(num))
        num = (sorted(num))

        s = int("".join(num[::2])) + int("".join(num[1::2]))
        return s


# You are given a 0-indexed array of string words and two integers left and right.
#
# A string is called a vowel string if it starts with a vowel character and ends with a vowel character
# where vowel characters are 'a', 'e', 'i', 'o', and 'u'.
#
# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].
def vowelStrings(words, left, right):
    vowels = "aeiou"
    res = 0
    for i in range(len(words)):
        if i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                res += 1
        elif i > right:
            break

    return res

# You are given a positive integer n.
#
# Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.
#
# Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.
#
# Return an integer array answer where answer = [even, odd].
def evenOddBit(n):

    binN = str(bin(n))[2:][::-1]
    res = [0, 0]

    for i in range(len(binN)):
        if binN[i] == "1":
            if i % 2 == 0:
                res[0] += 1
            else:
                res[1] += 1

    return res

# Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at
# least one digit from each array.
def minNumber(nums1, nums2):

    setCheck = set(nums1).intersection(set(nums2))

    if len(setCheck) > 0:
        return sorted(list(setCheck))[0]
    else:
        min1 = sorted(nums1)[0]
        min2 = sorted(nums2)[0]
        return int(str(min(min1, min2)) + str(max(min1, min2)))

# You are given a 0-indexed m x n integer matrix grid. The width of a column is the maximum length of its integers.
#
# For example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.
# Return an integer array ans of size n where ans[i] is the width of the ith column.
#
# The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise.
def findColumnWidth(grid):

    cols = []
    counter = 0
    while counter < len(grid[0]):
        temp = []
        for i in range(len(grid)):
            temp.append(len(str(grid[i][counter])))
        cols.append(temp)
        counter += 1

    res = []
    for i in cols:
        res.append(max(i))

    return res

# You are given a positive integer n, that is initially placed on a board. Every day, for 109 days,
# you perform the following procedure:
#
# For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
# Then, place those numbers on the board.
# Return the number of distinct integers present on the board after 109 days have elapsed.
#
# Note:
#
# Once a number is placed on the board, it will remain on it until the end.
# % stands for the modulo operation. For example, 14 % 3 is 2.
def distinctIntegers(n):

    if n != 1:
        return n - 1
    else:
        return 1

# You are given two 0-indexed integer arrays player1 and player2, that represent the number of pins that
# player 1 and player 2 hit in a bowling game, respectively.
#
# The bowling game consists of n turns, and the number of pins in each turn is exactly 10.
#
# Assume a player hit xi pins in the ith turn. The value of the ith turn for the player is:
#
# 2xi if the player hit 10 pins in any of the previous two turns.
# Otherwise, It is xi.
# The score of the player is the sum of the values of their n turns.
#
# Return
#
# 1 if the score of player 1 is more than the score of player 2,
# 2 if the score of player 2 is more than the score of player 1, and
# 0 in case of a draw.
def isWinner(player1, player2):

    if len(player1) == 1:
        p1 = player1[0]
        p2 = player2[0]

        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0

    p1, p2 = 0, 0
    for i in range(0, len(player1)):
        if (i > 0 and player1[i - 1] == 10) or (i > 1 and player1[i - 2] == 10):
            p1 += player1[i] * 2
        else:
            p1 += player1[i]

        if (i > 0 and player2[i - 1] == 10) or (i > 1 and player2[i - 2] == 10):
            p2 += player2[i] * 2
        else:
            p2 += player2[i]

    if p1 > p2:
        return 1
    elif p2 > p1:
        return 2
    else:
        return 0

#  You are given an integer array gifts denoting the number of gifts in various piles. Every second,
#  you do the following:
#
# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.
def pickGifts(gifts, k):

    for i in range(k):
        gifts = sorted(gifts)[::-1]
        gifts[0] = int(gifts[0] ** 0.5)

    return sum(gifts)

# You are given two 0-indexed integer arrays nums and divisors.
#
# The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].
#
# Return the integer divisors[i] with the maximum divisibility score. If there is more than one integer
# with the maximum score, return the minimum of them.
def maxDivScore(nums, divisors):

    res = []
    for i in divisors:
        div = 0
        for j in nums:
            if j % i == 0:
                div += 1

        res.append([div, i])

    res = sorted(res)[::-1]

    if len(res) > 1:
        if res[0][0] == res[1][0]:
            temp = []
            for i in res:
                if i[0] == res[0][0]:
                    temp.append(i[1])
            return min(temp)
        else:
            return res[0][1]
    else:
        return res[0][1]

# You are given a 0-indexed integer array nums.
#
# The concatenation of two numbers is the number formed by concatenating their numerals.
#
# For example, the concatenation of 15, 49 is 1549.
# The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:
#
# If there exists more than one number in nums, pick the first element and last element in nums respectively
# and add the value of their concatenation to the concatenation value of nums, then delete the first and
# last element from nums.
# If one element exists, add its value to the concatenation value of nums, then delete it.
# Return the concatenation value of the nums.
def findTheArrayConcVal(nums):

    res = 0
    while len(nums) > 0:
        if len(nums) > 1:
            res += int(str(nums[0]) + str(nums[-1]))
            nums.pop()
            nums.pop(0)
        else:
            res += nums[0]
            nums.pop()

    return res

# You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to
# another digit.
#
# Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.
#
# Notes:
#
# When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
# Bob can remap a digit to itself, in which case num does not change.
# Bob can remap different digits for obtaining minimum and maximum values respectively.
# The resulting number after remapping can contain leading zeroes.
def minMaxDifference(num):

    mx = []
    mn = []
    num = str(num)

    for i in set(num):
        maxTemp = []
        minTemp = []
        for j in range(len(num)):
            if num[j] == i:
                minTemp.append("0")
                maxTemp.append("9")
            else:
                maxTemp.append(num[j])
                minTemp.append(num[j])
        mx.append(int("".join(maxTemp)))
        mn.append(int("".join(minTemp)))

    return max(mx) - min(mn)

# You are given two 2D integer arrays nums1 and nums2.
#
# nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# Each array contains unique ids and is sorted in ascending order by id.
#
# Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
#
# Only ids that appear in at least one of the two arrays should be included in the resulting array.
# Each id should be included only once and its value should be the sum of the values of this id in the two arrays.
# If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.
#
#
def mergeArrays(nums1, nums2):

    res = []
    for i in nums1:
        for j in nums2:
            if i[0] == j[0]:
                i[1] += j[1]
                nums2.pop(nums2.index(j))

    for i in nums2:
        nums1.append(i)

    return sorted(nums1)

# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
#
# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.
# Where:
#
# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element,
# leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element,
# rightSum[i] = 0.
# Return the array answer.
def leftRightDifference(nums):

    leftSum = []
    rightSum = []
    for i in range(len(nums)):
        rightSum.append(sum(nums[i + 1:]))
        leftSum.append(sum(nums[0:i]))

    res = []
    for i in range(len(nums)):
        res.append(abs(leftSum[i] - rightSum[i]))

    return res

# There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.
#
# You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.
#
# The bag initially contains:
#
# numOnes items with 1s written on them.
# numZeroes items with 0s written on them.
# numNegOnes items with -1s written on them.
# We want to pick exactly k items among the available items. Return the maximum possible sum of
# numbers written on the items.
def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):

    lst = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
    return sum(lst[0:k])

# You are given a 0-indexed two-dimensional integer array nums.
#
# Return the largest prime number that lies on at least one of the diagonals of nums.
# In case, no prime is present on any of the diagonals, return 0.
#
# Note that:
#
# An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
# An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or
# an i for which nums[i][nums.length - i - 1] = val.

# SLOW
def diagonalPrime(nums):

    diag = []

    counterL = -1
    counterR = len(nums[0])
    for i in nums:
        counterL += 1
        counterR -= 1
        for j in range(len(i)):
            if j == counterL:
                diag.append(i[j])
            elif j == counterR:
                diag.append(i[j])

    prime = []
    for i in diag:
        if isPrime(i) == True:
            prime.append(i)

    if len(prime) > 0:
        return max(prime)
    else:
        return 0

def isPrime(num):
    prime = False

    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return prime
        else:
            prime = True
            return prime
    else:
        return prime

# FAST

def secondDiagonalPrimeFast(nums):

    res = 0
    n = len(nums)

    for i in range(n):
        if secondIsPrime(nums[i][i]):
            res = max(res, nums[i][i])
        if secondIsPrime(nums[i][n - i - 1]):
            res = max(res, nums[i][n - i - 1])

    return res

def secondIsPrime(self, num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# You are given a binary string s consisting only of zeroes and ones.
#
# A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal
# to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.
#
# Return the length of the longest balanced substring of s.
#
# A substring is a contiguous sequence of characters within a string.
def findTheLongestBalancedSubstring(s):

    subs = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            subs.add(s[i:j + 1])

    res = []
    for i in subs:
        if len(i) % 2 == 0:
            left = i[:len(i) // 2]
            right = i[len(i) // 2:]

            if left[0] == "0" and left.count(left[0]) == len(left):
                if right[0] == "1" and right.count(right[0]) == len(right):
                    res.append(len(i))

    if len(res) > 0:
        return max(res)
    else:
        return 0

# You are given a 0-indexed array of strings details. Each element of details provides information about a given
# passenger compressed into a string of length 15. The system is such that:
#
# The first ten characters consist of the phone number of passengers.
# The next character denotes the gender of the person.
# The following two characters are used to indicate the age of the person.
# The last two characters determine the seat allotted to that person.
# Return the number of passengers who are strictly more than 60 years old.
def countSeniors(details):

    res = 0
    for i in details:
        if "M" in i:
            temp = i.split("M")
            age = int(temp[1][:2])
        elif "F" in i:
            temp = i.split("F")
            age = int(temp[1][:2])
        else:
            temp = i.split("O")
            age = int(temp[1][:2])

        if age > 60:
            res += 1

    return res

# Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count
# of ones, and the number of ones in that row.
#
# In case there are multiple rows that have the maximum count of ones, the row with the smallest row number
# should be selected.
#
# Return an array containing the index of the row, and the number of ones in it.
def rowAndMaximumOnes(mat):

    numberOfOnes = []
    for i in range(len(mat)):
        numberOfOnes.append([mat[i].count(1), i])

    m = sorted(numberOfOnes)[-1][0]
    res = []

    for i in numberOfOnes:
        if i[0] == m:
            res.append(i[1])

    return [min(res), m]

# You are given a positive integer arrivalTime denoting the arrival time of a train in hours,
# and another positive integer delayedTime denoting the amount of delay in hours.
#
# Return the time when the train will arrive at the station.
#
# Note that the time in this problem is in 24-hours format.
def findDelayedArrivalTime(arrivalTime, delayedTime):

    res = arrivalTime + delayedTime

    if res <= 24:
        if res == 24:
            return 0
        else:
            return res
    else:
        return res - 24

# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5,
# or 7.
#
# Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
def sumOfMultiples(n):

    res = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            res += i

    return res

# You are given an integer array prices representing the prices of various chocolates in a store.
# You are also given a single integer money, which represents your initial amount of money.
#
# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money.
# You would like to minimize the sum of the prices of the two chocolates you buy.
#
# Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you
# to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.
def buyChoco(prices, money):

    prices = sorted(prices)

    if money - sum(prices[:2]) < 0:
        return money
    else:
        return money - sum(prices[:2])


# You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation
# exactly k times in order to maximize your score:
#
# Select an element m from nums.
# Remove the selected element m from the array.
# Add a new element with a value of m + 1 to the array.
# Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.
def maximizeSum(nums, k):

        nums = sorted(nums)[::-1]
        res = 0

        for i in range(k):
            res += nums[0]
            nums[0] += 1

        return res

# You are given a 0-indexed array nums of length n.
#
# The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of
# distinct elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the
# prefix nums[0, ..., i].
#
# Return the distinct difference array of nums.
#
# Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive.
# Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.
def distinctDifferenceArray(nums):
    res = []
    for i in range(len(nums)):
        res.append(len(set(nums[:i + 1])) - len(set(nums[i + 1:])))

    return res

# You are given a 0-indexed permutation of n integers nums.
#
# A permutation is called semi-ordered if the first number equals 1 and the last number equals n. You can perform
# the below operation as many times as you want until you make nums a semi-ordered permutation:
#
# Pick two adjacent elements in nums, then swap them.
# Return the minimum number of operations to make nums a semi-ordered permutation.
#
# A permutation is a sequence of integers from 1 to n of length n containing each number exactly once.
def semiOrderedPermutation(nums):

    if nums == sorted(nums):
        return 0
    else:
        minEl = nums.index(min(nums))
        maxEl = nums.index(max(nums))

        if minEl > maxEl:
            return minEl - maxEl + len(nums) - 2
        else:
            return minEl - maxEl + len(nums) - 1

# There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in
# clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n,
# and moving clockwise from the nth friend brings you to the 1st friend.
#
# The rules of the game are as follows:
#
# 1st friend receives the ball.
#
# After that, 1st friend passes it to the friend who is k steps away from them in the clockwise direction.
# After that, the friend who receives the ball should pass it to the friend who is 2 * k steps away from them in the
# clockwise direction.
# After that, the friend who receives the ball should pass it to the friend who is 3 * k steps away from them in the
# clockwise direction, and so on and so forth.
# In other words, on the ith turn, the friend holding the ball should pass it to the friend who is i * k steps away
# from them in the clockwise direction.
#
# The game is finished when some friend receives the ball for the second time.
#
# The losers of the game are friends who did not receive the ball in the entire game.
#
# Given the number of friends, n, and an integer k, return the array answer, which contains the losers of the game in
# the ascending order.
def circularGameLosers(n, k):

    res = []
    res.extend(range(1, n + 1))
    res.pop(0)

    ball = 1
    counter = 1

    while True:
        ball = (ball + (counter * k)) % n

        if ball == 0:
            ball = n

        if ball not in res:
            return res
        else:
            res.remove(ball)

        counter += 1

# You are given a string s consisting only of uppercase English letters.
#
# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of
# the substrings "AB" or "CD" from s.
#
# Return the minimum possible length of the resulting string that you can obtain.
#
# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.
def minLength(s):

    while "AB" in s or "CD" in s:
        s = s.replace("AB", "")
        s = s.replace("CD", "")

    return len(s)

# You are given two integers, num and t.
#
# An integer x is called achievable if it can become equal to num after applying the following operation no more than
# t times:
#
# Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
# Return the maximum possible achievable number. It can be proven that there exists at least one achievable number.
def theMaximumAchievableX(num, t):
    return num + t * 2

# You are given a string s consisting of lowercase English letters, and you are allowed to perform operations on it.
# In one operation, you can replace a character in s with another lowercase English letter.
#
# Your task is to make s a palindrome with the minimum number of operations possible. If there are multiple
# palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.
#
# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and
# b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
#
# Return the resulting palindrome string.
def makeSmallestPalindrome(s):

    s = list(s)

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            if s[i] < s[j]:
                s[j] = s[i]
            else:
                s[i] = s[j]
        i += 1
        j -= 1

    return "".join(s)

# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.
def removeTrailingZeros(num):

    if num[-1] == "0":
        while num[-1] == "0":
            num = num[:-1]

    return num

# You are given an integer n that consists of exactly 3 digits.
#
# We call the number n fascinating if, after the following modification, the resulting number contains all the digits
# from 1 to 9 exactly once and does not contain any 0's:
#
# Concatenate n with the numbers 2 * n and 3 * n.
# Return true if n is fascinating, or false otherwise.
#
# Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.
def isFascinating(n):

    res = ""
    res += str(n) + str(2 * n) + str(3 * n)

    if "".join(sorted(res)) == "123456789":
        return True
    else:
        return False


# Given a 0-indexed string s, repeatedly perform the following operation any number of times:
#
# Choose an index i in the string, and let c be the character in position i. Delete the closest occurrence of c to the
# left of i (if any) and the closest occurrence of c to the right of i (if any).
# Your task is to minimize the length of s by performing the above operation any number of times.
#
# Return an integer denoting the length of the minimized string.
def minimizedStringLength(s):

    return len(set(s))

# You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called
# beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.
#
# Return the total number of beautiful pairs in nums.
#
# Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. In other words,
# x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.
def countBeautifulPairs(nums):

    res = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if math.gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1:
                    res += 1

    return res

# Given an integer array nums containing distinct positive integers, find and return any number from the array that is
# neither the minimum nor the maximum value in the array, or -1 if there is no such number.
#
# Return the selected integer.
def findNonMinOrMax(nums):

    if len(nums) <= 2:
        return -1
    else:
        return sorted(nums)[1]

# You are given a 1-indexed integer array nums of length n.
#
# An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
#
# Return the sum of the squares of all special elements of nums.
def sumOfSquares(nums):

    res = 0
    n = len(nums)

    for i in range(n):
        i += 1
        if n % i == 0:
            res += nums[i - 1] ** 2

    return res

# You are given a 0-indexed array words consisting of distinct strings.
#
# The string words[i] can be paired with the string words[j] if:
#
# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.
#
# Note that each string can belong in at most one pair.
def maximumNumberOfStringPairs(words):

    res = 0
    for i in range(len(words)):
        words[i] = "".join(sorted(words[i]))

    for i in set(words):
        if words.count(i) == 2:
            res += 1

    return res

# A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in
# liters and additionalTank representing the fuel present in the additional tank in liters.
#
# The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional
# tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.
#
# Return the maximum distance which can be traveled.
#
# Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters
# consumed.
def distanceTraveled(mainTank, additionalTank):

    res = 0
    count = 1

    while mainTank > 0:

        if count == 5 and additionalTank > 0:
            mainTank += 1
            additionalTank -= 1
            count = 1
        else:
            count += 1

        res += 10
        mainTank -= 1

    return res

# You are given a 0-indexed integer array nums and an integer threshold.
#
# Find the length of the longest subarray of nums starting at index l and ending at index r (0 <= l <= r < nums.length)
# that satisfies the following conditions:
#
# nums[l] % 2 == 0
# For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
# For all indices i in the range [l, r], nums[i] <= threshold
# Return an integer denoting the length of the longest such subarray.
#
# Note: A subarray is a contiguous non-empty sequence of elements within an array.
def longestAlternatingSubarray(nums, threshold):

    res = 0
    for l in range(len(nums)):
        if nums[l] % 2 == 0 and nums[l] <= threshold:
            r = l
            while r + 1 < len(nums) and nums[r + 1] <= threshold and nums[r] % 2 != nums[r + 1] % 2:
                r += 1
            res = max(res, r - l + 1)

    return res

# You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:
#
# m is greater than 1.
# s1 = s0 + 1.
# The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words, s1 - s0 = 1, s2 - s1 = -1,
# s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2] = (-1)m.
# Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
def alternatingSubarray(nums):
    sub = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sub.append(nums[i:j])

    res = []
    for i in range(len(sub)):
        if len(sub[i]) > 1:
            if sub[i][1] > sub[i][0]:
                odd = []
                even = []
                for j in range(len(sub[i])):
                    if j % 2 == 0:
                        odd.append(sub[i][j])
                    else:
                        even.append(sub[i][j])

                if len(set(odd)) == len(set(even)) and len(set(odd)) == 1:
                    res.append(sub[i])

    if len(res) > 0:
        return len(max(res, key=len))
    else:
        return -1

def alternatingSubarray2(nums):
    mx = 0
    order = 1
    left = 0
    right = 1

    while True:
        if nums[right] - nums[right - 1] == order:
            right += 1
            order *= -1
        else:
            mx = max(mx, len(nums[left:right]))
            left += 1
            right = left + 1
            order = 1

        if right == len(nums):
            mx = max(mx, len(nums[left:right]))
            break

    return -1 if mx == 1 else mx

# There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the
# company.
#
# The company requires each employee to work for at least target hours.
#
# You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
#
# Return the integer denoting the number of employees who worked at least target hours.
def numberOfEmployeesWhoMetTarget(hours, target):

    res = 0
    for i in hours:
        if i >= target:
            res += 1

    return res

# Given an array of strings words and a character separator, split each string in words by separator.
#
# Return an array of strings containing the new strings formed after the splits, excluding empty strings.
#
# Notes
#
# separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
# A split may result in more than two strings.
# The resulting strings must maintain the same order as they were initially given.
def splitWordsBySeparator(words, separator):

    res = []
    for i in words:
        temp = i.split(separator)
        for j in temp:
            if j != "":
                res.append(j)

    return res


# Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you
# have written. Typing other characters works as expected.
#
# You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.
#
# Return the final string that will be present on your laptop screen.
def finalString(s):

    res = ""
    for i in list(s):
        if i == "i":
            res = res[::-1]
        else:
            res += i

    return res

# You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].
#
# base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1
# exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].
#
# Return true if the given array is good, otherwise return false.
#
# Note: A permutation of integers represents an arrangement of these numbers.
def isGood(nums):

    n = max(nums)
    perm = [i for i in range(1, n + 1)]
    perm.append(perm[-1])

    if sorted(nums) == perm:
        return True
    else:
        return False

# You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums
# such that the maximum digit in both numbers are equal.
#
# Return the maximum sum or -1 if no such pair exists.
def maxSum(nums):

    pairs = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            iMax = max(str(nums[i]))
            jMax = max(str(nums[j]))

            if i != j and iMax == jMax:
                if sorted([nums[i], nums[j]]) not in pairs:
                    pairs.append(sorted([nums[i], nums[j]]))

    sm = 0
    for i in pairs:
        sm = max(sm, sum(i))

    if sm == 0:
        return -1
    else:
        return sm


# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0
# <= i < j < n and nums[i] + nums[j] < target.
def countPairs(nums, target):

    res = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] + nums[j] < target:
                res += 1

        return res

# Initially, you have a bank account balance of 100 dollars.
#
# You are given an integer purchaseAmount representing the amount you will spend on a purchase in dollars.
#
# At the store where you will make the purchase, the purchase amount is rounded to the nearest multiple of 10.
# In other words, you pay a non-negative amount, roundedAmount, such that roundedAmount is a multiple of 10 and
# abs(roundedAmount - purchaseAmount) is minimized.
#
# If there is more than one nearest multiple of 10, the largest multiple is chosen.
#
# Return an integer denoting your account balance after making a purchase worth purchaseAmount dollars from the store.
#
# Note: 0 is considered to be a multiple of 10 in this problem.
def accountBalanceAfterPurchase(purchaseAmount):

    if len(str(purchaseAmount)) == 2:

        firstDigit = int(str(purchaseAmount)[0])
        secondDigit = int(str(purchaseAmount)[1])

        if secondDigit >= 5:
            firstDigit += 1
            purchaseAmount = int(str(firstDigit) + str("0"))
        if secondDigit < 5:
            purchaseAmount = int(str(firstDigit) + str("0"))

    if len(str(purchaseAmount)) == 1:

        if purchaseAmount >= 5:
            purchaseAmount = 10
        if purchaseAmount < 5:
            purchaseAmount = 0

    return 100 - purchaseAmount

# Given an array of strings words and a string s, determine if s is an acronym of words.
#
# The string s is considered an acronym of words if it can be formed by concatenating the first character of each
# string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from
# ["bear", "aardvark"].
#
# Return true if s is an acronym of words, and false otherwise.
def isAcronym(words, s):

    res = []
    for i in words:
        res.append(i[0])

    return "".join(res) == s

# You are given two positive integers low and high.
#
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum
# of the last n digits of x. Numbers with an odd number of digits are never symmetric.
#
# Return the number of symmetric integers in the range [low, high].
def countSymmetricIntegers(low, high):

    res = 0
    for i in range(low, high + 1):
        num = str(i)
        if len(num) % 2 == 0:
            left = 0
            right = 0
            for i in range(len(num) // 2):
                left += int(num[i])
                right += int(num[-(i + 1)])

            if left == right:
                res += 1

    return res


# You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.
#
# You can apply the following operation on any of the two strings any number of times:
#
# Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.
def canBeEqual(s1, s2):

    if sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2]):
        return True
    else:
        return False

# You are given a string moves of length n consisting only of characters 'L', 'R', and '_'.
# The string represents your movement on a number line starting from the origin 0.
#
# In the ith move, you can choose one of the following directions:
#
# move to the left if moves[i] = 'L' or moves[i] = '_'
# move to the right if moves[i] = 'R' or moves[i] = '_'
# Return the distance from the origin of the furthest point you can get to after n moves.
def furthestDistanceFromOrigin(moves):

    lCount = moves.count("L")
    rCount = moves.count("R")
    uCount = moves.count("_")

    if lCount >= rCount:
        return abs(lCount - rCount) + uCount
    else:
        return abs(rCount - lCount) + uCount


# You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line.
# For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the
# ending point of the ith car.
#
# Return the number of integer points on the line that are covered with any part of a car.
def numberOfPoints(nums):

    intersect = []
    for i in nums:
        for j in range(i[0], i[1] + 1):
            if j not in intersect:
                intersect.append(j)

    return len(intersect)

# You are given an array nums of positive integers and an integer k.
#
# In one operation, you can remove the last element of the array and add it to your collection.
#
# Return the minimum number of operations needed to collect elements 1, 2, ..., k.
#
#
def minOperations(nums, k):

    nums = nums[::-1]
    collection = [i for i in range(1, k + 1)]
    res = 0
    for i in nums:
        if i in collection:
            collection.remove(i)
            res += 1
        else:
            res += 1
        if len(collection) == 0:
            return res


# You are given a 0-indexed array nums of length n containing distinct positive integers. Return the minimum
# number of right shifts required to sort nums and -1 if this is not possible.
#
# A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.
def minimumRightShifts(nums):

    res = 0
    for i in range(len(nums)):

        if sorted(nums) == nums:
            return res

        last = [nums[-1]]
        nums = last + nums[:-1]
        res += 1

    if sorted(nums) == nums:
        return res

    return -1

# You are given a binary string s that contains at least one '1'.
#
# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number
# that can be created from this combination.
#
# Return a string representing the maximum odd binary number that can be created from the given combination.
#
# Note that the resulting string can have leading zeros.
def maximumOddBinaryNumber(s):

    last = sorted(s)[-1]
    other = sorted(s)[:-1][::-1]

    return "".join(other) + "".join(last)

def maximumOddBinaryNumberSecond(s):

    ones = s.count("1")
    zeros = s.count("0")

    if ones == 1:
        return "0" * zeros + "1"
    else:
        return "1" * (ones - 1) + "0" * zeros + "1"


# You are given a 0-indexed integer array nums and an integer k.
#
# Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits
# in their binary representation.
#
# The set bits in an integer are the 1's present when it is written in binary.
#
# For example, the binary representation of 21 is 10101, which has 3 set bits.
def sumIndicesWithKSetBits(nums, k):

    res = []
    for i in range(len(nums)):
        if str(bin(i)[2:]).count("1") == k:
            res.append(nums[i])

    return sum(res)


# You are given a string array words and a binary array groups both of length n, where words[i] is associated with
# groups[i].
#
# Your task is to select the longest alternating
# subsequence
#  from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their
#  corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent
#  elements have non-matching corresponding bits in the groups array.
#
# Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ...,
# ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these
# indices.
#
# Return the selected subsequence. If there are multiple answers, return any of them.
#
# Note: The elements in words are distinct.
def getLongestSubsequence(words, groups):

    res = []
    current = -1

    for word, group in zip(words, groups):
        if group != current:
            res.append(word)
            current = group

    return res


# You are given a 0-indexed integer array nums.
#
# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have
# a negative value, return 0.
#
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
def maximumTripletValue(nums):

    mx = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i < j < k:
                    mx = max((nums[i] - nums[j]) * nums[k], mx)

    return mx

# You are given a 0-indexed integer array nums.
#
# The distinct count of a subarray of nums is defined as:
#
# Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length.
# Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
def sumCounts(nums):

    subs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subs.append(set(nums[i:j]))

    res = 0
    for i in subs:
        res += len(i) ** 2

    return res

# Given an integer array nums where nums[i] is either a positive integer or -1. We need to find for each -1 the
# respective positive integer, which we call the last visited integer.
#
# To achieve this goal, let's define two empty arrays: seen and ans.
#
# Start iterating from the beginning of the array nums.
#
# If a positive integer is encountered, prepend it to the front of seen.
# If -1 is encountered, let k be the number of consecutive -1s seen so far (including the current -1),
# If k is less than or equal to the length of seen, append the k-th element of seen to ans.
# If k is strictly greater than the length of seen, append -1 to ans.
# Return the array ans.
def lastVisitedIntegers(nums):

    seen = []
    res = []
    k = 0
    for i in nums:
        if i != -1:
            seen.append(i)
            k = 0
        else:
            k += 1
            if k <= len(seen):
                res.append(seen[-k])
            else:
                res.append(-1)

    return res


# You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer
# valueDifference.
#
# Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:
#
# abs(i - j) >= indexDifference, and
# abs(nums[i] - nums[j]) >= valueDifference
# Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise.
# If there are multiple choices for the two indices, return any of them.
#
# Note: i and j may be equal.
def findIndices(nums, indexDifference, valueDifference):

    for i in range(len(nums)):
        for j in range(len(nums)):
            if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                return [i, j]

    return [-1, -1]

# You are given positive integers n and m.
#
# Define two integers, num1 and num2, as follows:
#
# num1: The sum of all integers in the range [1, n] that are not divisible by m.
# num2: The sum of all integers in the range [1, n] that are divisible by m.
# Return the integer num1 - num2.
def differenceOfSums(n, m):

    num1 = 0
    num2 = 0
    for i in range(1, n + 1):
        if i % m == 0:
            num2 += i
        else:
            num1 += i

    return num1 - num2

# You are given a 0-indexed array nums of integers.
#
# A triplet of indices (i, j, k) is a mountain if:
#
# i < j < k
# nums[i] < nums[j] and nums[k] < nums[j]
# Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.
def minimumSum(nums):

    res = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i < j < k:
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        res.append(nums[i] + nums[j] + nums[k])
    if len(res) > 0:
        return min(res)
    else:
        return -1

# You are given an integer array nums, and an integer k. Let's introduce K-or operation by extending the standard
# bitwise OR. In K-or, a bit position in the result is set to 1 if at least k numbers in nums have a 1 in that position.
#
# Return the K-or of nums.
def findKOr(nums, k):

    bit = []
    m = 0

    for i in nums:
        bit.append(list(bin(i)[2:]))
        m = max(m, len(list(bin(i)[2:])))

    for i in range(len(bit)):
        if len(bit[i]) != m:
            while len(bit[i]) < m:
                bit[i] == bit[i].insert(0, 0)

    res = [0 for i in range(len(bit[0]))]

    for i in bit:
        for j in range(len(i)):
            res[j] += int(i[j])

    for i in range(len(res)):
        if res[i] < k:
            res[i] = "0"
        else:
            res[i] = "1"

    return int("".join(res), 2)


# There are n teams numbered from 0 to n - 1 in a tournament.
#
# Given a 0-indexed 2D boolean matrix grid of size n * n. For all i, j that 0 <= i, j <= n - 1 and i != j team i is
# stronger than team j if grid[i][j] == 1, otherwise, team j is stronger than team i.
#
# Team a will be the champion of the tournament if there is no team b that is stronger than team a.
#
# Return the team that will be the champion of the tournament.
def findChampion(grid):

    res = []
    for i in grid:
        res.append(i.count(1))

    return res.index(max(res))








