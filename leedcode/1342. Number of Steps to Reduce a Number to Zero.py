#https://donic0211.medium.com/leetcode-1342-number-of-steps-to-reduce-a-number-to-zero-9850bb844971

import math
class Solution:
    def numberOfSteps (self, num):
        step=0
        while(num>0):
            if num % 2 ==0:
                num=num//2
            else:
                num-=1
            step+=1
        return step