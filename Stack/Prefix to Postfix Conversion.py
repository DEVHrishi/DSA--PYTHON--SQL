'''
Input: 
*-A/BC-/AKL
Output: 
ABC/-AK/L-*'''

class Solution:

    def preToPost(self, pre_exp):

        s=[] 

        for i in pre_exp[::-1]:

            if i.isalpha():

                s.append(i)

            else:

                a=s.pop()

                b=s.pop()

                s.append(a+b+i)

        return s[0]