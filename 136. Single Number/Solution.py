class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # for i in range(len(nums)):
        #      if(nums.count(nums[i])==1):
        #         return nums[i]
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
           
        return nums[-1]
