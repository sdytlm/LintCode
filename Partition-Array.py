class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if len(nums) == 0:
            return 0
        front = 0
        
        for i in range(len(nums)):
            if nums[i] < k and front < len(nums):
                nums[i],nums[front] = nums[front],nums[i]
                front += 1
   
        for i in range(len(nums)):
            if nums[i] >= k:
                return i
        return len(nums)
