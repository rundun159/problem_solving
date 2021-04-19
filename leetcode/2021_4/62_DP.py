import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.cache = [[-1 for i in range(n)] for j in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    self.cache[r][c] = 1
        return self.dp(m - 1, n - 1)

    def dp(self, r, c):
        if self.cache[r][c] != -1:
            return self.cache[r][c]
        ret = self.dp(r - 1, c) + self.dp(r, c - 1)
        self.cache[r][c] = ret
        return ret

