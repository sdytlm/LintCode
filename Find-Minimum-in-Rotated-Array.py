class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if num == None or len(num) == 0:
            return 0
        front = 0
        end = len(num)-1

        result = sys.maxint
        while front <= end and front >=0:
            mid = (front+end)/2
            # case 1: no in orded subarray
            if num[front] > num[end] :
                front = mid+1
            else:
                # case 2: already in a orded subarray, search for the lowest value
                if result > num[front]:
                    result = num[front]
                front -= 1
                end = mid - 1

        return result
