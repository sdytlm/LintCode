class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if s1 == None or s2 == None or s3 == None:
            return False
        
        l1 = len(s1)+1
        l2 = len(s2)+1
        l3 = len(s3)+1
        
        if l3 != l1+l2-1:
            return False
        
        dp = [[False] * l2 for i in range(l1)]
        
        # init dp if s1,s2,or s3 could be empty
        for i in range(l1-1):
            dp[i+1][0] = s1[:i+1]==s3[:i+1]

        for i in range(l2-1):
            dp[0][i+1] = s2[:i+1]==s3[:i+1]

        dp[0][0] = True        
        for i in range(len(s1)):
            for j in range(len(s2)):
                dp[i+1][j+1] = False
                # s3 choose s1
                if s3[i+j+1] == s1[i]:
                    dp[i+1][j+1] = dp[i][j+1]
                # s3 choose s2
                if s3[i+j+1] == s2[j]:
                    dp[i+1][j+1] |= dp[i+1][j]
                
        return dp[l1-1][l2-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.isInterleave("aab","a","aaab")
