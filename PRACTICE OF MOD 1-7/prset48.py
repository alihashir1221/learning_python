'''
Exercise 10. Finding Extremes (Min/Max) in a List
Practice Problem: Given a list of integers, find and print both the largest and the smallest numbers.
Exercise Purpose: This exercise explores “Aggregate Functions.” While Python has built-in tools for this, understanding how to identify extremes is critical for data normalization, where you often need to find the range of a dataset before processing it.

Given Input: nums = [45, 2, 89, 12, 7]
Expected Output: Largest: 89 Smallest: 2
'''
def aggregate(nums):
    maximum = max(nums)
    minimum = min(nums)
    print(f"The maximum number from the list is {maximum} and the minimum number from the list is {minimum}")
    
nums = [45, 2, 89, 12, 7]
aggregate(nums)

