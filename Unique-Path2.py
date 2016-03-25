class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        # dp[i][j]: # of path at <i,j>
        # dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + 1
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[1]*(col+1) for i in range(row+1)]

        for i in range(1,row+1):
            for j in range(1,col+1):
                #dp[0][0]
                if i==1 and j==1:
                    dp[i][j] = 1-obstacleGrid[i-1][j-1]
                #dp[1][j]
                elif i==1:
                    if obstacleGrid[i-1][j-1]==1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j-1]
                #dp[i][1]
                elif j==1:
                    if obstacleGrid[i-1][j-1]==1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j]
                #dp[i][j]
                else:
                    if obstacleGrid[i-1][j-1] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[i][j]

