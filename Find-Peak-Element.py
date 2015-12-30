class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if not A:
            return 0
        front = 0
        end = len(A)-1

        while front <= end:
            mid = (front+end)/2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] < A[mid-1]:
                end = mid-1
            else:
                front = mid + 1
        return 0


