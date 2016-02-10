class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here

        hash_map = dict()
        
        for i in nums:
            if hash_map.has_key(i):
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        
        max = 0
        result = 0
        for i in nums:
            if hash_map[i] > max:
                max = hash_map[i]
                result = i
        return result
