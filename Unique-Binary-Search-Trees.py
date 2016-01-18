class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        # count[n]: number of unique binary search trees for n numbers
        # count[n] = sum(count[i]*[n-1-i]) i in [0,n-1]
        # count[3] = count[0]*count[2] + count[1]*count[1] + count[2]*count[0]
        if n < 2:
            return 1
        count = [0] * (n+1)
        count[0] = 1
        count[1] = 1

        for i in range(2,n+1): # [0,n]
            for j in range(0,i): #[0,i)
                count[i] += count[j]*count[i-1-j]
        return count[n]
