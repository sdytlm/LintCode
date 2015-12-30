class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        # a in [0,m*n-1]
        # matrix[i][j] = matrix[a/cols][a%cols]
        front = 0
        end = rows*cols-1

        while front <= end:
            mid = (front+end)/2
            if matrix[mid/cols][mid%cols] == target:
                return True
            elif matrix[mid/cols][mid%cols] < target:
                front = mid+1
            else:
                end = mid-1
        return False
