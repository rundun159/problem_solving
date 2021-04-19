class Solution:
    def uniquePaths(self, m, n):
        new_m = m-1
        new_n = n-1
        max_mn = max(new_m, new_n)
        min_mn = min(new_m, new_n)
        dividened = 1
        sum_mn = new_m + new_n
        for i in range(max_mn+1, sum_mn+1):
            dividened *= i
        return int(dividened/self.factorial(min_mn))
    def factorial(self, int):
        ret = 1
        for i in range(1,int+1):
            ret *= i
        return ret