# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def topSort(self, graph):
        indegree = {}
        ret = []
        queue = []
        # indegree <graphnode, degree> 
        for x in graph:
            indegree[x] = 0
        # count indegree
        for i in graph:
            for j in i.neighbors:
                indegree[j] = indegree[j]+1
        # find the starer
        for i in graph:
            if indegree[i] == 0:
                ret.append(i)
                queue.append(i)
        # bfs: use queue (use bfs in my code)
        # dfs: use recursive
        while len(queue) != 0:
            cur = queue[0]
            queue.pop(0)
            for i in cur.neighbors:
                indegree[i] -= 1
                if indegree[i] == 0:
                    ret.append(i)
                    queue.append(i)
        return ret
