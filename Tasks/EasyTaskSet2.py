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

