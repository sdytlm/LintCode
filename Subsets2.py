class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subset_helper(self,numbers,solution,result):
        # get one solution
        result.append(solution[:])
        for i,en in enumerate(numbers):
            # remove duplicated cases
            if i >0 and numbers[i] == numbers[i-1]:
                continue

            solution.append(en)
            self.subset_helper(numbers[i+1:],solution,result)
            solution.pop()
        return


    def subsetsWithDup(self, S):
        # write your code here
        result = []
        self.subset_helper(sorted(S),[],result)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([0]))
