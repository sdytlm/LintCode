class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        result = []
        if nums == None or len(nums) == 0:
            return result
            
        for i in range(len(nums)):
            # [1,2,3,0] => [3,3] is correct
            if nums[i] == 0:
                return [i,i]
            sum = nums[i]
            for j in range(i+1, len(nums)):
                if sum + nums[j] == 0:
                    result.append(i)
                    result.append(j)
                    return result
                else: 
                    sum += nums[j]
        return result
