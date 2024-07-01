class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums) - 1, 3):
            if nums[i] != nums[i+1] and nums[i+2]:
                return nums[i]
           
        return nums[-1]