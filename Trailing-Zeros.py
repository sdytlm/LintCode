class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        num = 0
        # if use i**5 to compare with n
        # you will out of boundary of Int
        while n/5 >= 1:
            num += n/5
            n = n/5
        return num
