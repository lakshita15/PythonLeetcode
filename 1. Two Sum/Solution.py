class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_list = []
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):  # Iterate from i + 2 to avoid duplicates
                if nums[i] + nums[j] == target:
                    new_list.append(i)
                    new_list.append(j)
                    break  # Exit inner loop after finding the first pair
            if len(new_list) > 0:  # Exit outer loop if a pair is found
                break
        return new_list