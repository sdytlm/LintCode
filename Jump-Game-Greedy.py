class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if A == None or len(A) == 0:
            return False

        index_true = len(A) - 1
        
        for i in range(len(A)-1,-1,-1):
            if i+A[i] >= index_true:
                index_true = i
        if index_true == 0:
            return True
        else:
            return False


