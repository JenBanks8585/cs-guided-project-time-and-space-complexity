"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    a = [x for x in nums if nums.count(x) ==1]
    return a

print(single_number([5,2,3,2,3]))
print(single_number([10]))
print(single_number([3,3,2,1]))


