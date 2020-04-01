# Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

# assume all indexes have just integers
# assume all integers are positive.

# decalre target number
# declare array of numbers
# iterate through array and add each number 
# repeat until sum is equal to target number 
# return the sum value
nums = [2, 4, 5, 7]
target = 9

for i in range(len(nums)):
    left = nums[i+1:]
    for j in range(len(left)):
        if (nums[i] + left[j]) == target:
            return i, j+i+1