# https://donic0211.medium.com/leetcode-1464-maximum-product-of-two-elements-in-an-array-f6ad991c4a38

class Solution:
    def maxProduct(self, nums):
        l=len(nums)
        nums=sorted(nums,reverse=True)
        return (nums[0]-1)*(nums[1]-1)
        