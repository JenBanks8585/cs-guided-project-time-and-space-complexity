"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
#Option1
def two_sum(nums, target):
    for i in nums:
         for j in nums:
             if i + j == target and nums.index(i)!= nums.index(j):
                 return [nums.index(i), nums.index(j)]

print(two_sum(nums = [2,5,9,13], target = 7))
print(two_sum(nums = [4,3,5], target = 8))


#Option2
def two_sum1(nums, target):
    for i,v in enumerate(nums):
        for j,w in enumerate(nums):
            if v + w ==target and i != j:
                return [i,j]

print(two_sum1(nums = [2,5,9,13], target = 7))
print(two_sum1(nums = [4,3,5], target = 8))