class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        paths = [[0] * n for i in range(m)]
        paths[0][0] = 1
        if n==1 or m<=1:
            return 1
        for i in range(0, m):
            paths[i][0] = 1
        for i in range(0, n):
            paths[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]
