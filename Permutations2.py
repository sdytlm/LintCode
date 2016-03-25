class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permutation(self,entry,result,solution):
        if len(entry) == 0:
            if solution not in result:
                result.append(solution[:])
            return
        for i in range(len(entry)):
            element = entry[i]
            solution.append(element)
            entry.pop(i)
            self.permutation(entry,result,solution)
            solution.pop()
            entry.insert(i,element)
        return

    def permuteUnique(self, nums):
        # write your code here
        result = []
        if nums == None or len(nums) == 0:
            return result
        self.permutation(nums,result,[])
        return result
