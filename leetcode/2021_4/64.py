class Solution:
    def minPathSum(self, grid) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.cache = [[-1 for i in range(self.n)] for j in range(self.m)]
        self.cache[0][0] = self.grid[0][0]
        self.max_int = 1<<31 -1
        return self.dp(self.m-1,self.n-1)
    def dp(self,r,c):
        if r < 0 or r >= self.m or c<0 or c >= self.n:
            return self.max_int
        if self.cache[r][c] != -1:
            return self.cache[r][c]
        ret = self.max_int
        ret = min(ret, self.dp(r-1,c)+self.grid[r][c])
        ret = min(ret, self.dp(r,c-1)+self.grid[r][c])
        self.cache[r][c] = ret
        return ret