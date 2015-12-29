class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if nums==None or len(nums)==0:
            return -1
        front = 0
        end = len(nums) - 1

        result = sys.maxint
        while front <= end:
            mid = (front+end)/2
            if nums[mid] == target:
                # we cannot guarantee this "mid" is the first position
                if result > mid:
                    result = mid
                # we can check the previous pos
                end = mid-1

            elif nums[mid] > target:
                end = mid-1
            else:
                front = mid+1
        
        if result == sys.maxint:
            return -1
        else:
            return result
