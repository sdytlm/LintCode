class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here
        # Build the mask
        if j < 31:
            ones = ~0 # 2**32 - 1
            # [0,end] = 11111111100000000000000
            left = ones << (j+1) # Note, you shit j+1 bit to make [i,j] is 0
            # [0,i) = 111111
            right = (1 << i) - 1
            # mask = 11111111100000000111111
            mask = left | right
        else: # j+1 = 32 (> max_int), then mask = right
            mask = (1 << i) - 1
        return (mask & n) | (m<<i)

