class TH:
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)
        self.cache = [-1 for i in nums]

    def dp(self, idx):
        if idx >= self.len:
            return 0
        if self.cache[idx] != -1:
            return self.cache[idx]
        ret = self.nums[idx]
        for next_idx in range(idx + 2, self.len):
            ret = max(ret, self.dp(next_idx) + self.nums[idx])
        self.cache[idx] = ret
        return ret


class Solution:
    def rob(self, nums) -> int:
        th = TH(nums)
        for i in range(th.len):
            th.dp(i)
        ret = -1
        for i in th.cache:
            ret = max(ret, i)
        return ret