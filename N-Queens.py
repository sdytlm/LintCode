class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def validPos(self,i,j,n,solution):
        if i == 0:
            return True
        row_index = 0
        for row in solution:
            col_index = row.find('Q')
            # same col
            if col_index == j:
                return False
            # diagonal
            if col_index-row_index == j-i or col_index+row_index == j+i:
                return False
            row_index += 1
        return True
    
    def recursiveNQ(self, result,solution,row,row_index,n):
        if n == row_index:
            tmp_sol =[]
            for i in solution:
                tmp_sol.append(i)
            result.append(tmp_sol)
            return

        for j in range(n):
            # check if <i,j> can be put Q
            if self.validPos(row_index,j,n,solution) == True:
                # create a new row
                row_new = ""
                for i in range(j):
                    row_new += "."
                row_new += "Q"
                for i in range(n-j-1):
                    row_new += "."
                solution.append(row_new)
                # check another line
                self.recursiveNQ(result,solution,row_new,row_index+1,n)
                solution.pop()

        return
    

    def solveNQueens(self, n):
        # write your code here
        if n < 1:
            return None
        if n == 1:
            return [['Q']]
        
        result = []
        solution = []
        # init solution
        row = ""
        for i in range(n):
            row += "."
        self.recursiveNQ(result,solution,row,0,n)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(10))
