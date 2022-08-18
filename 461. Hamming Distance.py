class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while True:
            if x==0 and y==0:
                break
            num1 = x&1
            num2 = y&1
            if num1 != num2:
                ans += 1
            x >>= 1
            y >>= 1
        return ans