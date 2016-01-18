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
        i = n/2
        while i>0:
            for j in range(i):
                array[n/i] *= array[n/(2*i)] 
            array[n/i] %= b
            if i==1:
                return array[n]
            if i/2 == 0:
                return array[n/i]
            i = i/2
            print array

if __name__ == "__main__":
    Sol = Solution()
    Sol.fastPower(3,5,7)
