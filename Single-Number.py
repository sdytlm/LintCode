class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    #根据x^x=0 和x^0=x 可将给定数组的所有数依次异或,最后保留的即为结果
    def singleNumber(self, A):
        # write your code here
        sum = 0
        for i in A:
           sum ^= i
        return sum
