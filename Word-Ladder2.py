class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    def buildpath(self, path, prevMap,word,result):
        if len(prevMap[word]) == 0:
            path.append(word)
            curPath = path[:]
            curPath.reverse()
            result.append(curPath)
            path.pop()
            return
        path.append(word)
        for iter in prevMap[word]:
            self.buildpath(path,prevMap,iter,result)
        path.pop()
    def FindLadders(self, start, end, dict):
        result = []
        # <dict[i]:path>
        prevMap = {}
        length = len(start)
        # init prevMap <dict[i]: []>
        # [] represents all string before prevMap
        for i in dict:
            prevMap[i] = []

        # candidates[[], []]
        candidates = [set(), set()]
        cur = 0
        prev = 1
        # add start into candidate[current]
        candidates[cur].add(start)
        # BFS
        while True:
            # exchange cur,prev
            cur,prev = prev,cur
            # remove current string from dict
            for i in candidates[prev]:
                dict.remove(i)
            candidates[cur].clear()

            for word in candidates[prev]:
                for i in range(length):
                    left = word[:i]
                    right = word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            newword = left+j+right
                            if newword in dict:
                                prevMap[newword].append(word)
                                candidates[cur].and(newword)
            if len(candidates[cur]) == 0:
                return result
            if end in candidates[cur]:
                break
        buildpath([],prevMap,end,result)
        return result

