class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine_helper(self,result,entry,n,k,index,starter):
        if index == k:
            # if you use entry, later if you change entry, the result will be changed.
            new_entry = []
            for j in entry:
                new_entry.append(j)
            result.append(new_entry)
            return

        for i in range(starter,n+1):
            entry.append(i)
            self.combine_helper(result,entry,n,k,index+1,i+1)
            entry.pop()
        return

    def combine(self, n, k):      
        # write your code here 
        entry = []
        result = []
        if k > n or n < 1:
            return result
       
        self.combine_helper(result,entry,n,k,0,1)
        return result

