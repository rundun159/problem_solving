from collections import defaultdict, deque
class Node:
    def __init__(self):
        self.incoming = 0
        self.outgoing = []

class TH:
    def __init__(self, numCourses, prerequisites):
        self.numCourses = numCourses
        self.prerequisites = prerequisites
        self.no_incoming = deque()
        self.graph = defaultdict(Node)
        self.num_edges = len(prerequisites)
        self.deleted_edges = 0
        for p in prerequisites:
            prev , next = p[1] , p[0]
            self.graph[prev].outgoing.append(next)
            self.graph[next].incoming += 1
        for t in self.graph.items():
            if t[1].incoming == 0:
                self.no_incoming.append(t[0])
    def topological_sort(self):
        while self.no_incoming:
            prev = self.no_incoming.popleft()
            while self.graph[prev].outgoing:
                next = self.graph[prev].outgoing.pop()
                self.graph[next].incoming -= 1
                self.deleted_edges += 1
                if self.graph[next].incoming == 0:
                    self.no_incoming.append(next)
        if self.num_edges == self.deleted_edges:
            return True
        else:
            return False

    def print_nodes(self):
        for i in self.graph.items():
            print('key : ' + str(i[0]) + ' values outgoing : ' + str(i[1].outgoing) + 'incoming : ' + str(i[1].incoming))

class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        th = TH(numCourses, prerequisites)
        th.print_nodes()
        return th.topological_sort()
# sol = Solution()
# print(sol.canFinish( 2, [[1,0]] ))