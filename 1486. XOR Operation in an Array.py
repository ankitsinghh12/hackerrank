#https://donic0211.medium.com/leetcode-1486-xor-operation-in-an-array-287ff91ddb68

class Solution:
    def xorOperation(self, n, start):
        ans=0
        for i in range(n):
            ans^=(start+i*2)
        
        return ans