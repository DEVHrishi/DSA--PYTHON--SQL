'''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3'''

# top-down
# tc: O(n) and sc: O(n)
class Solution:
    def fun(self, nums, i, dp):
        if i >= len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]
        steal = nums[i] + self.fun(nums, i+2, dp)
        skip = self.fun(nums, i+1, dp)

        dp[i] = max(steal, skip)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        dp = [-1] * len(nums)
        dp1 = [-1] * len(nums)
        return max(self.fun(nums[1:], 0, dp), self.fun(nums[:-1], 0, dp1))

# bottom-up
# tc: O(n) and sc: O(n)
class Solution:
    def robber(self, nums):
        dp = [-1] * (len(nums))
        dp[0]  = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        return max(self.robber(nums[:-1]), self.robber(nums[1:]))
    
# space optimized
# tc: O(n) and sc: O(1)
class Solution:
    def robber(self, nums):
        a = nums[0]
        b = max(nums[:2])
        c = 0

        for i in range(2, len(nums)):
            c = max(b, nums[i]+a)
            a = b
            b = c
        return c
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(self.robber(nums[:-1]), self.robber(nums[1:]))