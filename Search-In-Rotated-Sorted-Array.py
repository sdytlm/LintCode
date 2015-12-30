class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        front = 0
        end = len(A) - 1

        while front<=end:
            mid = front + (end-front)/2
            if A[mid] == target:
                return mid
            # Case 1: [A[front], A[mid]] is sorted
            if A[front] < A[mid]:
                # A[mid] > target, then target could be in another subarray or [A[front], A[mid]]
                if A[mid] > target and A[front] <= target:
                    end = mid-1
                # A[mid] too large
                else:
                    front = mid+1
            else:
            # Case 2: [A[front],A[end]] is sorted
                    # any values of left subarray are larger than right subarray 
                    # A[mid] < target, value could be in [A[mid] ...] or [A[front] ... pivot]
                    # Go left
                    if A[mid] < target and A[end] >= target:
                        front = mid+1
                    else:
                        end = mid-1
        return -1
