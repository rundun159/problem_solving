import math, sys
sys.setrecursionlimit(10000000)

class Solution:
    def __init__(self):
        self.sqrs = [None for x in range(101)]
        for i in range(101):
            self.sqrs[i] = i*i
        self.cache = [None]*10001
    def numSquares(self, n: int) -> int:
        return self.f(n)
    def f(self, num):
        if self.cache[num]:
           return self.cache[num]
        max_cand_idx = int(math.sqrt(num))
        max_cand_value = self.sqrs[max_cand_idx]
        if max_cand_value == num:
            self.cache[num] = 1
            return 1
        cand = math.inf
        for idx in reversed(range(1,max_cand_idx+1)):
            now_val = self.sqrs[idx]
            left_val = num - self.sqrs[idx]
            ret = self.f(left_val)
            cand = min(cand, ret+1 )

        self.cache[num] = cand
        return cand
#
# sol = Solution()
# print(sol.numSquares(12))