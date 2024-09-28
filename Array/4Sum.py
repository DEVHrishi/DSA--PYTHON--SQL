'''Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = set()
        for i in range(n-3):
            for j in range(i+1, n-2):
                l = j+1
                r = n - 1
                while l < r:
                    total = nums[i]+ nums[j]+ nums[l]+ nums[r]
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        print(i, j, l, r)
                        result.add(tuple([nums[i], nums[j], nums[l], nums[r]]))
                        l += 1
                        r -= 1
        return list(result)