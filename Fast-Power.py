# Recursive
class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n==0:
            return 1%b
        if n==1:
            return a%b
        result = self.fastPower(a,b,n/2)
        result = (result * result)%b
        # 若n是奇数，需要多乘一次
        if n%2 == 1:
            result = (result*a)%b
        return result

# Array
class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        # (a * b) % p = ((a % p ) * (b % p)) % p
        if n==0:
            return 1%b
        array = [1] * (n+1)
        array[0] = 1%b
        array[1] = a%b
        for i in range(2,n+1):
            j = i
            while j>0:
                if j==1:
                    array[i] *= array[1]
                    break
                else:
                    array[i] *= array[j/2];
                    j -= j/2 
            array[i] %= b
        return array[n]

