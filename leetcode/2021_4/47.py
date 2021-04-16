from collections import defaultdict
class TH:
    def __init__(self, nums):
        self.nums = nums
        self.ret = []
        self.cnt = [0 for i in range(21)]
        dict = defaultdict(bool)
        for n in nums:
            self.cnt[n+10] += 1
            dict[n] = True
        self.new_nums = []
        for i in range(21):
            if self.cnt[i]:
                self.new_nums.append(i-10)
    def dfs(self, remain, stack):
        if remain == 0:
            self.ret.append(list(stack))
            return
        for idx, v in enumerate(self.new_nums):
            if self.cnt[v+10] != 0:
                self.cnt[v+10] -= 1
                stack.append(v)
                self.dfs(remain -1, stack)
                self.cnt[v+10] += 1
                stack.pop()


class Solution:
    def permuteUnique(self, nums) :
        th = TH(nums)
        th.dfs(len(nums),[])
        return th.ret