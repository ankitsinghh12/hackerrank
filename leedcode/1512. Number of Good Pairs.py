#https://donic0211.medium.com/leetcode-1512-number-of-good-pairs-a285a07a68e1


class Solution:
    def numIdenticalPairs(self, nums):
        f={}
        ans=0
        for num in nums:
            if not num in f:
                f[num]=0
            f[num]+=1
        
        for num in f:
            n=f[num]
            ans+=(n*(n-1)//2)
            
        return ans