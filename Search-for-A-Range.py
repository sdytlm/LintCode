class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here

        if A==None or len(A)==0:
            return [-1,-1]
        index1 = sys.maxint
        index2 = -1
        front = 0
        end = len(A) - 1

        
        # binary search for index1
        while front<=end :
            mid = (front+end)/2
            if A[mid] == target:
                # if you find target, should check the previous element
                end = mid-1
                if index1 > mid:
                    index1 = mid
            elif A[mid] > target:
                end = mid-1
            else:
                front = mid+1

        # binary search for index2
        front = 0
        end = len(A)-1

        while front<=end :
            mid = (front+end)/2
            if A[mid] == target:
                # if you find target, should check the next element
                front = mid+1
                if index2 < mid:
                    index2 = mid
            elif A[mid] > target:
                end = mid-1
            else:
                front = mid+1
        if index1 == sys.maxint or index2 == -1:
            return [-1,-1]
        else:
            return [index1, index2]

