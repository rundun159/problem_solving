from collections import defaultdict
class TH:
    def __init__(self, candidates, target):
        self.candidates = candidates
        self.target = target
        self.cache = [None for i in range(self.target+1)]
        self.cache[0] = [[]]
    def dp(self, val):
        if val < 0 :
            return -1
        if self.cache[val] != None:
            return self.cache[val]
        ret = []
        for idx, c in enumerate(self.candidates):
            tmp_ret = self.dp(val - c)
            if tmp_ret != -1:
                for tmp in tmp_ret:
                    ret.append([i for i in tmp]+ [c])
        if len(ret) == 0 :
            self.cache[val] = -1
            return -1
        self.cache[val] = ret
        return ret
class Solution:
    def combinationSum(self, candidates, target):
        th = TH(candidates, target)
        th.dp(target)
        ret = []
        idx_dict = defaultdict(int)
        idx = 0
        for idx, v in enumerate(candidates):
            idx_dict[v] = idx
        if th.cache[target] == -1:
            return []
        for cand in th.cache[target]:
            tmp_ret = [0 for i in candidates]
            for c in cand:
                tmp_ret[idx_dict[c]] += 1
            tmp_ret2 = []
            for idx, t in enumerate(tmp_ret):
                for i in range(t):
                    tmp_ret2.append(candidates[idx])
            found = False
            for r in ret:
                if tmp_ret2 == r:
                    found = True
                    break
            if not found:
                ret.append(tmp_ret2)
        return ret