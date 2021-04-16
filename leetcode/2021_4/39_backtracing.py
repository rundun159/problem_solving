class Solution:
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        len_cand = len(candidates)
        ret = []

        def dfs(remain, comb, start):
            if remain < 0:
                return
            if remain == 0:
                ret.append(list(comb))
                return
            for next in range(start, len_cand):
                comb.append(candidates[next])
                dfs(remain - candidates[next], comb, next)
                comb.pop()

        dfs(target, [], 0)
        return ret