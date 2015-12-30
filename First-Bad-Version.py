#classSVNRepo:                                                              
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can useSVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.

class Solution:
    """
     @param n: An integers.
     @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # your code here
        front = 1
        end = n
        result = sys.maxint
        while front <= end:
            mid = (front+end)/2
            if SVNRepo.isBadVersion(mid) == True:
                end = mid-1
                if result > mid:
                    result = mid
            else:
                front = mid + 1
        return result
