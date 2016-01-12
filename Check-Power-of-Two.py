class Solution:
    #
    # @param n: An integer
    # @return: True or false
    #
    # if x & x-1 == 0, then x is the power of 2
    def checkPowerOf2(self, n):
        if n < 1:
            return False
        if (n & (n-1)) == 0:
            return True
        else:
            return False
    
