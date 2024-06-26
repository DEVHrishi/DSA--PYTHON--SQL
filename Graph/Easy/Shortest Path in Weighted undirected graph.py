'''You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges describing there are edges between a to b with some weight, find the shortest path between the vertex 1 and the vertex n and if path does not exist then return a list consisting of only -1.

Note - 
1. If there exists a path, then return a list whose first element is the weight of the path.
2. If no path exists then return a list containing a single element -1.

Example:
Input:
n = 5, m= 6
edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
Output:
5 1 4 3 5
Explaination:
Shortest path from 1 to n is by the path 1 4 3 5 whose weight is 5. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function shortestPath() which takes n vertex and m edges and vector of edges having weight as inputs and returns the shortest path between vertex 1 to n.

Expected Time Complexity: O(m* log(n))
Expected Space Complexity: O(n)'''

from typing import List
import heapq
from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, start, end, weight):
        self.graph[start].append((end, weight))
        self.graph[end].append((start, weight))
        
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])
        
        dist = [float('inf')] * (n+1)
        parent = [i for i in range(n+1)]
        min_heap = [(0, 1)]
        dist[1] = 0
        
        while min_heap:
            current_dist, u = heapq.heappop(min_heap)
            
            if current_dist > dist[u]:
                continue
            
            for v, weight in self.graph[u]:
                d = current_dist + weight
                if dist[v] > d:
                    dist[v] = d
                    heapq.heappush(min_heap, (d, v))
                    parent[v] = u

        if dist[n] == float('inf'):
            return [-1]
        result = []
        node = n
        while node != parent[node]:
            result.append(node)
            node = parent[node]
        
        result.extend([1, dist[n]])

        return result[::-1]
        