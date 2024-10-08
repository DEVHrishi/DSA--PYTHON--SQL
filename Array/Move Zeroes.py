'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            if nums[i] != 0:
                i += 1
                j += 1
            elif nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                
class Solution:
	def moveZeroes(self, nums: List[int]) -> None:

		p,q=0,0
		while q<len(nums):
			if nums[q]==0:
				q=q+1
			else:
				nums[p],nums[q]=nums[q],nums[p]
				p=p+1
				q=q+1

		return nums