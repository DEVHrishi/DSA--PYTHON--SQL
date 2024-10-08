'''Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prev = [-1]*n
        next = [n]*n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                next[top] = i
            if stack:
                prev[i] = stack[-1]
            stack.append(i)
        area = 0
        for j in range(n):
            area = max(area, (next[j]-prev[j]-1)*heights[j])
        return area