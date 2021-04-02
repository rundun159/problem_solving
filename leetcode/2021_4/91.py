import sys
sys.setrecursionlimit(100000)
class GIVEN_STRING:
    def __init__(self,s):
        self.len = len(s)
        self.s = s
        self.cache = [-1]*self.len
    def f(self, idx):
        if idx >= self.len:
            return 0
        if idx == self.len-1:
            if self.s[idx] != '0':
                self.cache[idx] = 1
                return 1
        if self.cache[idx] != -1:
            return self.cache[idx]
        else:
            if self.s[idx] == '0':
                self.cache[idx]=0
                return 0
            else:
                ret = 0
                ret += self.f(idx+1)
                if int(self.s[idx:idx+2]) <= 26:
                    ret += self.f(idx+2)
                    if idx+2 == self.len:
                        ret += 1
                self.cache[idx] = ret
                return ret
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        gs = GIVEN_STRING(s)
        # return gs.f(0)
        print(gs.f(0))

sol = Solution()
sol.numDecodings("10101")
sol.numDecodings("1")
sol.numDecodings("12")
sol.numDecodings("123")
