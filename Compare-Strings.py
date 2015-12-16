class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        # an array to carry all characters
        characters = [0] * 256
        
        for i in range(len(A)) :
            index = ord(A[i]) - ord('A')
            characters[index] += 1
        
        for i in range(len(B)) :
            index = ord(B[i]) - ord('A')
            if characters[index] == 0:
                return False
            characters[index] -= 1
        
        return True
