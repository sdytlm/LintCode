class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        # hash_map: {sum: index}
        hash_map = dict()
        hash_map[0] = 0
        result = []
        if nums == None or len(nums) == 0:
            return result

        sum = 0
        for i in range(len(nums)):
            # case <x, x, x, 0, x, x>
            if nums[i] == 0:
                result.append(i)
                result.append(i)
                return result
            
            sum += nums[i]
            # if you find sum again
            # <hash_map[sum],x,x,x,i> is the substring you are looking for
            if(hash_map.has_key(sum)):
                result.append(hash_map[sum])
                result.append(i)
                return result
            else:
                hash_map[sum] = i+1
        return result
