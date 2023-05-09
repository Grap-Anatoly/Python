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






