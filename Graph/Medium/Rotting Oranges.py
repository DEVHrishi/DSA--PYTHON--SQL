'''You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Directions for moving in the grid
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        fresh_oranges = 0
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # If there are no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0
        
        minutes_passed = -1  # Starting with -1 because we increment at the start of the loop
        
        # BFS process
        while queue:
            minutes_passed += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2  # Rot the fresh orange
                        fresh_oranges -= 1
                        queue.append((new_row, new_col))
        
        # If there are still fresh oranges left, return -1
        return minutes_passed if fresh_oranges == 0 else -1