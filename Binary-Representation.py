class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        # write you code here
        result = ""
        integer = 0
        decimal = 0
        if n==None:
            return result
        # Parse the integer and decimal
        dot_index = n.find(".")
        left = n[0:dot_index]
        right = n[dot_index+1:len(n)]
        if left!=None and left!='0':
            integer = int(left)
        if right!=None and right!='0':
            decimal = int(right)
        
        # Translate to hex
        # int part
        if integer == 0:
            result = "0"
        else:
            while integer!=0:
                digit = integer%2
                result = str(digit) + result
                integer = integer/2
        
        integer_len = len(result)
        
        # decimal part
        # eg. 5.0
        if decimal == 0:
            return result
        else:
            result += "."
            decimal = float("0."+right)
            while decimal!=0.0:
                digit = int(decimal*2)
                result = result+str(digit)
                # decimal can only be 32bit at most
                if len(result)-integer_len >= 32:
                    return "ERROR"
                if decimal*2 >= 1.0:
                    decimal = decimal*2 - 1.0
                else:
                    decimal = decimal*2
        return result
