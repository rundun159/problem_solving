class Solution:
    def combinationSum3(self, k: int, n: int) :
        ret = []
        candidates = [i for i in range(0, 10)]

        def backtrack(remain, comb, start):
            if remain < 0:
                return
            elif remain == 0 and len(comb) == k:
                ret.append(list(comb))
                return
            for next in range(start + 1, 10):
                comb.append(next)
                backtrack(remain - next, comb, next)
                comb.pop()

        backtrack(n, [], 0)
        return ret