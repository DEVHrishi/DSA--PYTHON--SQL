'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d'''

from itertools import zip_longest

# TC = O(max(N, M)) and sc = O(n+m)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str1=""
        i=0
        j=0
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                str1+=word1[i]
                i+=1
            if j<len(word2):
                str1+=word2[j]
                j+=1
        return str1

# TC = O(min(N, M)) and sc = O(n+m)
def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1),len(word2))
        st = ""
        for i in range(n):
            st += word1[i]+word2[i]
        return st+word1[n:]+word2[n:]

# TC = O(max(N, M)) and sc = O(n+m)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        return ''.join(a+b for a, b in zip_longest(word1, word2, fillvalue=''))