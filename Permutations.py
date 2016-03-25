class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute_helper(self,result,solution,nums):
        if len(nums)==0:
            result.append(solution[:])
            return
        for i in range(len(nums)):
            el = nums[i]
            solution.append(el)
            nums.pop(i)
            self.permute_helper(result,solution,nums)
            solution.pop()
            nums.insert(i,el)
        return


    def permute(self, nums):
        # write your code here
        result = []
        if nums == None or len(nums) == 0:
            return result
        self.permute_helper(result,[],nums)
        return result 

if __name__ == "__main__":
    sol = Solution()
    sol.permute([1])
