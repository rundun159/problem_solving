from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        self.s = s
        self.cache = [None for i in range( len(s))]
        self.len = len(s)
        self.dict = defaultdict(bool)
        for w in wordDict:
            self.dict[w] = True
        return self.f(0)
    def f(self,idx):
        if idx == self.len:
            return True
        if self.cache[idx] != None:
            return self.cache[idx]
        # print("cache : ", self.cache[idx])
        now_s = ''
        now_s = self.s[idx:min(idx+20,self.len)]
        # print(idx, now_s)
        for i in reversed(range(1,len(now_s)+1)):
            # print(now_s[0:i])
            if self.dict[now_s[0:i]]:
                if self.f(idx + i ):
                    self.cache[idx] = True
                    return True
        self.cache[idx] = False
        return False
                # now_s = ''

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
dict= ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

# # s = "leetcode"
# # dict = ['leet','code']
sol = Solution()
print(sol.wordBreak(s, dict))