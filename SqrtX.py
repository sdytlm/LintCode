class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        front = 0
        end = x
        if x == 0 or x == 1:
            return x
        result = 0
        while front <= end:
            mid = (front+end)/2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                end = mid-1
            else:
                front = mid+1
        # x=2147483647, return 46340
        return front-1
