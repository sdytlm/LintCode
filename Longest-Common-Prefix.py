class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        result = ""
        if strs == None :
            return result
        if len(strs) == 0:
            return result 

        min_len = sys.maxint
        min_str = 0
        for i in range(len(strs)):
            if min_len > len(strs[i]):
                min_len = len(strs[i])
                min_str = i
        if min_len == 0:
            return result
        for i in range(len(strs[min_str])):
            for index in range(len(strs)) :
                if strs[min_str][i] != strs[index][i]:
                    return result
            result += strs[min_str][i]
                
        return result
