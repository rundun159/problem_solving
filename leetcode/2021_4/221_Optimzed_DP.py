class TH:
    def __init__(self,matrix):
        self.matrix = [[int(r) for r in row] for row in matrix]
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
    def optimized_dp(self):
        dp = self.matrix[0][:]
        ret = 0
        for d in dp:
            ret = max(ret, d)
        if self.rows > 1 and self.cols > 1:
            for r_idx in range(1, self.rows):
                print("before DP", dp)
                print("now row", self.matrix[r_idx])
                print(" ")
                prev = dp[0]
                ret = max(ret, self.matrix[r_idx][0])
                for c_idx in range(1, self.cols):
                    tmp = dp[c_idx]
                    if self.matrix[r_idx][c_idx]:
                        dp[c_idx] = min(min(dp[c_idx -1], dp[c_idx]),prev ) + 1
                        ret = max(ret, dp[c_idx])
                    else:
                        dp[c_idx] = 0
                    prev = tmp
                print("after DP", dp)
                print(" ")
            return ret * ret
        else:
            ret = 0
            for row in self.matrix:
                for v in row:
                    ret = max(ret, v)
            return ret

class Solution(object):
    def maximalSquare(self, matrix):
        th = TH(matrix)
        # th.dp_recursion()
        # return th.ret
        return th.optimized_dp()
# sol = Solution()
# # val = sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
# val = sol.maximalSquare([["1"]])
#
# print (val)
