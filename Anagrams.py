class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        # hash_map: hash map indexed by sorted_str
        # sorted_str: a list of strings matching strs
        # return_strs: a list of return strings
        hash_map = dict()
        sorted_str = []
        for unsorted_str in strs:
            tmp_str = ''.join(sorted(unsorted_str))
            sorted_str.append(tmp_str)
            if tmp_str in hash_map:
                hash_map[tmp_str] += 1
            else:
                hash_map[tmp_str] = 1
        
        return_strs = [strs[i] for i in range(len(strs)) if hash_map[sorted_str[i]] > 1]
        return return_strs
