class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False
    
        str_len = len(s)
        
        # declare an array for alphabet and other special characters lists
        alphabet = [0] * 256
       
        # count number of appearance for each letter in s and t
        for i in range(0, str_len):
            alphabet[ord(s[i]) - ord('a')] += 1
            alphabet[ord(t[i]) - ord('a')] += 1

        for i in range(0,26):
            if alphabet[i] % 2 != 0:
                return False
        return True 
