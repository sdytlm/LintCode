class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here
        if A==None:
            return None
        
        count=0
        stack = []
        for i in A:
            while len(stack)!=0 and stack[len(stack)-1]>i and k>0: 
                stack.pop()
            	k -= 1
                # cannot append i if i is '0' and s is empty
                # case: 90249, 2
                # but if s is not empty, we could append '0'
                # case 100000045, 4
            if i!='0' or len(stack)!=0:
                stack.append(i)
        result =""
        for i in stack:
            result += i
        
        if k==0:
            return result
        else:
            # result is larger than expected
            return result[0:len(result)-k]
