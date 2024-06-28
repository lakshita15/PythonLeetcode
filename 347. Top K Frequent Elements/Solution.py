class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count frequency of each element
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Collect all keys and their frequencies
        freq_list = []
        for key in freq.keys():
            freq_list.append((key, freq[key]))
        
        # Step 3: Sort by frequency in descending order
        freq_list.sort(key=lambda x: x[1], reverse=True)
        
        # Step 4: Extract the top k elements
        top_k_elements = []
        for i in range(k):
            top_k_elements.append(freq_list[i][0])
        
        return top_k_elements
