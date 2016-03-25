ass Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subset_helper(self,result,solution,nums):
        result.append(solution[:])
                        
        for i,el in enumerate(nums):
            solution.append(el)
            self.subset_helper(result,solution,nums[i+1:])
            solution.pop()
                                                                                return
                                                                                
                                                                                def subsets(self, S): 
        # write your code here
                                                                                    result = []             
                                                                                    self.subset_helper(result,[],sorted(S))
                                                                                    return result
                                                                                                                        
