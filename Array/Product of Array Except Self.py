'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 1
        r = 1
        result = [0]*n
        for i in range(len(nums)):
            result[i] = l
            l *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            result[j] = r * result[j]
            r *= nums[j]
        
        return result
            