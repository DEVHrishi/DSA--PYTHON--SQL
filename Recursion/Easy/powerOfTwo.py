'''Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1'''

# recursive approach
def isPowerOfTwo(self, n: int) -> bool:
    if n==0:
        return False
    if n==1:
        return True
    elif n%2==0:
        return self.isPowerOfTwo(n//2)
    
    

# iterative approach
def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0 and (n & (n-1) == 0))