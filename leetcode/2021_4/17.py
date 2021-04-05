DATA = {}
DATA['2']=['a','b','c']
DATA['3']=['d','e','f']
DATA['4']=['g','h','i']
DATA['5']=['j','k','l']
DATA['6']=['m','n','o']
DATA['7']=['p','q','r','s']
DATA['8']=['t','u','v']
DATA['9']=['w','x','y','z']
class TH:
    def __init__(self, digits):
        self.cand_lists = []
        for d in digits:
            self.cand_lists.append(DATA[d])
        self.len = len(digits)
        self.ret = []
        self.now_str = []
    def bfs_main(self):
        if self.len ==0:
            return []
        else:
            self.bfs(0)
            return self.ret
    def add_str(self):
        now_ret=""
        for i in self.now_str:
            now_ret += i
        self.ret.append(now_ret)
        return
    def bfs(self, idx):
        if idx == self.len:
            self.add_str()
            return
        for i in self.cand_lists[idx]:
            self.now_str.append(i)
            self.bfs(idx+1)
            self.now_str.pop()
        return
class Solution:
    def letterCombinations(self, digits: str):
        th = TH(digits)
        return th.bfs_main()