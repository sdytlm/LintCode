class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        B = []
        if A == None or len(A) == 0:
            return B
        
        for i in range(len(A)):
            sum = 1
            for j in range(len(A)):
                if i != j:
                    sum *= A[j]
            B.append(sum)
        return B
