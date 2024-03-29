'''Given two integers dividend and divisor. Find the quotient after dividing dividend by divisor without using multiplication, division and mod operator.

Example 1:

Input:
a = 10, b= 3
Output: 3
Exaplanation:
10/3 gives quotient as 3 
and remainder as 1.
Example 2:

Input:
a = 43, b = -8
Output: -5
Explanation:
43/-8 gives quotient as -5 and 
remainder as 3.
Your task:
You don't have to read input or print anything. Your task is to complete the function divide() which takes two integers a and b as input and returns the quotient after dividing a by b.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)'''

import math
class Solution:
    def divide(self, a, b):
        #code here
        divd=abs(a)
        divs=abs(b)
        s=0
        p=math.floor(math.log2(divd))+1
        while(divs<=divd):
            if((divs<<p)<=divd):
                s+=1<<p
                divd-=(divs<<p)
            p-=1
        if(a<0 and b>0) or(a>0 and b<0):
            return -s
        return s