class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.s_len = len(s)
        self.cache = [[None for i in range(self.s_len)] for j in range(self.s_len)]
        max_len = 1
        max_s = 0
        max_e = 0
        for i in range(self.s_len):
            self.cache[i][i] = True
        for s in range(self.s_len):
            for e in range(s+1,self.s_len):
                if self.dp(s,e):
                    if max_len < (e-s+1):
                        max_s , max_e = s,e
                        max_len = (e-s+1)
        ret = ''
        for i in range(max_s,max_e+1):
            ret += self.s[i]
        return ret
    def dp(self,s,e):
        if e >= self.s_len:
            return False
        if s>e:
            return False
        if s==e:
            return True
        if e == (s+1):
            return self.s[s] == self.s[e]
        if self.cache[s][e] != None:
            return self.cache[s][e]
        self.cache[s][e] = (self.s[s] == self.s[e]) and self.dp(s+1,e-1)
        # if self.s[s] == self.s[e]:
        #     self.cache[s][e] = self.dp(s+1,e-1)
        # else:
        #     self.cache[s][e] = False
        return self.cache[s][e]