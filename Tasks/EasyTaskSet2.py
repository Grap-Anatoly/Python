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
