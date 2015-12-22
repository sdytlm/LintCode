class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        if A == None or len(A) == 0:
            return 1
        length = len(A)
        # The first missing positive should in [1...N]
        # Scan A, if A[i] <= 0 or A[i] > N, we assign a dummy integer -1

        for i in range(length):
            if A[i] <= 0 or A[i] > length:
                A[i] = -1

        # Use Aray A as hash table, if A[i] in [1...N], we put A[i] to A[A[i]-1]
        # A[i] != A[A[i]-1] is used for removing dead loop if A = [1]
        for i in range(length):
            while A[i] != -1 and A[i] != A[A[i]-1]:
                tmp = A[A[i]-1]
                A[A[i]-1] = A[i]
                A[i] = tmp
        # Scan the new A, find A[i] != i+1
        for i in range(length):
            if A[i] != i+1:
                return i+1
                
        # for case: [1,2,3], missing is 4
        return length+1
