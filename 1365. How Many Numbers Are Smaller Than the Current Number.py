
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # There are two ways to copy nums to nums1
        # nums1 = [x for x in nums] # Method 1
        nums1 = copy.deepcopy(nums) # Method 2
        
        nums1.sort() # After sorting, the subscript of the number is how many numbers are less than it

        res = []
        for num in nums:
            res.append(nums1.index(num))
        return res