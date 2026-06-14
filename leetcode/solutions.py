# Problem 1: Two Sum
# Input: list of integers and a target number
# Output: indices of the two numbers that add up to the target
# Approach: brute force - check every pair of numbers

def twoSum (self, nums, target):
        for i in range(len(nums)): 
            for j in range(len(nums)): 
               if nums[i] + nums[j] == target and i != j: 
                return [i, j] 