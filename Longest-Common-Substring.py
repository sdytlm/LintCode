class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        row = len(A)
        col = len(B)
        dp = [[0]*col for i in range(row)]
        result = 0

        for i in range(row) :
            for j in range(col) :
                if A[i] != B[j] :
                    dp[i][j] = 0
                else :
                    if (i==0) or (j==0) :
                        dp[i][j] = 1
                    else :
                        dp[i][j] = dp[i-1][j-1] + 1
                if result<dp[i][j]:
                    result = dp[i][j]
        
        return result
        
