'''Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16'''

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        l, r = 0, n - 1
        val = 0
        while l < r:
            val += (nums[r] - nums[l])
            l+= 1
            r -= 1
        return val
    
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        med = (nums[n//2]+nums[n//2 - 1])//2 if n % 2 == 0 else nums[n // 2]
        val = 0
        for i in nums:
            val += abs(i-med)
        return val