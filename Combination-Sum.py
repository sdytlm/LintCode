class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def comb_helper(self,candidates,target,result,entry,sum):
        if sum > target:
            return 
        if sum == target:
            tmp = []
            for j in entry:
                tmp.append(j)
            result.append(tmp)
            return
        for i in candidates:
            entry.append(i)
            self.comb_helper(candidates,target,result,entry,sum+i)
            entry.pop()
        return
    
    def combinationSum(self, candidates, target):
        # write your code here
        result = []
        entry = []
        if candidates == None:
            return result
        self.comb_helper(candidates,target,result,entry,0)
        
        # remove the duplicated answer
        ret = []
        for i in result:
            i = sorted(i)
            if i not in ret:
                ret.append(i)
        return ret
        

