class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # seen = set()
        # unique = []
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #     else:
        #         seen.remove(num)  # Remove duplicates from seen set
        # unique = list(seen)  # Convert set to list for return type
        # return unique

        seen_once = []  # List to store elements seen once (potential unique)
        
        for num in nums:
            if num not in seen_once :
                seen_once.append(num)
            elif num in seen_once:
                seen_once.remove(num)  # Remove from seen_once if seen twice
                

        return seen_once  # Assuming the first two unique elements are desired
