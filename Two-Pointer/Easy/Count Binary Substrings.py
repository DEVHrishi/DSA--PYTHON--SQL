'''Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.'''

# tc = O(n) and sc = O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev = 0
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                count += min(prev, curr)
                prev = curr
                curr = 1
        count += min(prev, curr)
        return count