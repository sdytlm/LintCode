class Solution:
    def strStr(self, source, target):
        # write your code here
        j = 0
       
        # None string is NULL
        if source == None or target == None:
            return -1
        
        # target is empty
        if target == "":
            return 0
        
        for i in range(len(source)) :
            source_index = i
            while target[j] == source[source_index] and j < len(target) :
                source_index += 1
                j += 1
                if j == len(target) :
                    return i
            j = 0
        return -1
