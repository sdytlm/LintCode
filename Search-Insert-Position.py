class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        front = 0
        end = len(A) - 1
        while front<=end:
            mid = (front+end)/2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid-1
            else:
                front = mid+1
        return front
