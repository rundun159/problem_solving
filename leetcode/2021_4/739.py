class Solution:
    def dailyTemperatures(self, T ) :
        self.ret = [None for t in T]
        self.len = len(T)
        self.ret[-1] = 0
        for idx1 in reversed(range(self.len-1)):
            done = False
            idx2 = idx1+1
            while idx2 < self.len and not done:
                x1,x2 = T[idx1], T[idx2]
                diff = idx2 -idx1
                if x1 < x2:
                    self.ret[idx1] = diff
                    done = True
                else:
                    if self.ret[idx2] == 0 :
                        self.ret[idx1] = 0
                        done = True
                    else:
                        idx2 += self.ret[idx2]
        return self.ret

# sol = Solution()
# print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
