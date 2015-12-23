class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A==None or len(A)==0:
            return 0
        start=0
        for i in range(len(A)):
            # find the non-duplicate element
            # update A[start+1]
            if A[i] != A[start]:
                start += 1
                A[start] = A[i]
            
        return start+1
