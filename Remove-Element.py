class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        result = len(A)
        if A == None or len(A) == 0:
            return A
        while elem in A:
            A.remove(elem)
        return len(A)
