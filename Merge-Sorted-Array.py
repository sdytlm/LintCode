class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if n == 0:
            return
        index = m+n-1
        i = m-1
        j = n-1
        while i>=0 and j>=0:
            if A[i] >= B[j]:
                A[index] = A[i]
                i -= 1
                index -= 1
            else:
                A[index] = B[j]
                j -= 1
                index -= 1
        while j>=0:
            A[index] = B[j]
            j -= 1
            index -= 1
        return 
            

