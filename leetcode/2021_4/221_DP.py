class TH:
    def __init__(self,matrix):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.cache = [[int(r) for r in row] for row in self.matrix]
        self.ret = 0

    def dp_recursion(self):
        for r_idx, row in enumerate(self.matrix):
            for c_idx, v in enumerate(row):
                if v:
                    self.ret = max(1, self.ret)
                    cand_positions = [[r_idx-1, c_idx -1], [r_idx-1, c_idx], [r_idx, c_idx-1]]
                    min_width = 1<<31 -1
                    fail_larger = False
                    for cand_pos in cand_positions:
                        if cand_pos[0]>=0 and cand_pos[0] < self.rows and cand_pos[1] >=0 and cand_pos[1] < self.cols:
                            if self.cache[cand_pos[0]][cand_pos[1]] == 0:
                                fail_larger = True
                                break
                            else:
                                min_width = min(min_width, self.cache[cand_pos[0]][cand_pos[1]])
                    if not fail_larger:
                        self.cache[r_idx][c_idx] = min_width +1
                        self.ret = max(self.ret, min_width +1)
class Solution(object):
    def maximalSquare(self, matrix):
        th = TH(matrix)
        th.dp_recursion()
        return th.ret
# sol = Solution()
# # val = sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
# val = sol.maximalSquare([["1"]])
#
# print (val)
