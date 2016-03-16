import collections
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        # queue: <word,level>
        queue = collections.deque([(start,1)])
        # if you dont add end into the dict, you will never find the final destination
        dict.add(end)

        while len(queue) != 0:
            curr = queue.popleft()
            level = curr[1]
            cur = curr[0]
            if cur == end:
                return level
            else:
                wordL = list(cur)
                for i in 'abcdefghijklmnopqrstuvwxyz':
                    for j in range(len(wordL)):
                        left_word = cur[:j]
                        right_word = cur[j+1:]
                        if i != cur[j]:
                            # new_word is the word may exist in the dict
                            new_word = left_word+i+right_word
                            if new_word in dict:
                                queue.append((new_word,level+1))
                                dict.remove(new_word)
        return 0
