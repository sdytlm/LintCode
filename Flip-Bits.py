class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        result = 0
        # if a<0, then a's binary is 2^32 - abs(a)
        if a < 0:
            a = 2**32 + a
        if b < 0:
            b = 2**32 + b
        while a!=0 or b!=0:
            if a%2 != b%2:
                result +=1
            a /= 2
            b /= 2
        return result


