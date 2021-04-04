class TH:
    def __init__(self,matrix):
        self.M = len(matrix)
        self.N = len(matrix[0])
        self.matrix = [[None for x in range(self.N)] for y in range(self.M)]
        self.prev = []
        self.next = []
        self.size = 1
        for i in range(self.M):
            for j in range(self.N):
                if matrix[i][j]=='1':
                    self.matrix[i][j] = 1
                    self.prev.append([i,j])
                else:
                    self.matrix[i][j] = 0
        self.small = min(self.M,self.N)

    def do_main(self):
        if len(self.prev) == 0:
            return 0
        for i in range(self.small):
            if not self.check_step():
                return (self.size - 1) * (self.size - 1)
        return (self.size -1 ) * (self.size -1)

    def check_step(self):
        ret = False
        for pos_idx in range(len(self.prev)):
            if self.do_step(pos_idx):
                ret = True
                self.next.append(self.prev[pos_idx])
        if ret:
            self.size += 1
            del self.prev
            self.prev = self.next
            # del self.next
            self.next = []
            return True
        else:
            return False

    def do_step(self, idx):
        pos = self.prev[idx]
        right_most = [pos[0], pos[1]+self.size-1]
        below_most = [pos[0]+self.size-1, pos[1]]
        if right_most[1] >= self.N or below_most[0] >= self.M:
            return False
        for i in range(pos[0] , pos[0] + self.size):
            if not self.matrix[i][right_most[1]]:
                return False
        for i in range(pos[1] , pos[1] + self.size):
            if not self.matrix[below_most[0]][i]:
                return False
        return True

class Solution(object):

    def maximalSquare(self, matrix):
        th = TH(matrix)
        return th.do_main()

        """
        :type matrix: List[List[str]]
        :rtype: int
        """
#
# sol = Solution()
# # val = sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
# val = sol.maximalSquare([["1"]])
#
# print (val)
