'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        count = 0
        h, w = 0 , 0

        for i in range(n):
            while stack and height[stack[-1]] <= height[i]:
                top = stack.pop()
                if stack:
                    h = min(height[stack[-1]], height[i]) - height[top]
                    w = i - stack[-1] - 1
                    count += h*w
            
            stack.append(i)
        
        return count