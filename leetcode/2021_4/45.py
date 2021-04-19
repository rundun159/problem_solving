class TH:
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)
        self.max_int = 1 << 31 - 1
        self.cache = [None for i in nums]

    def dp(self, idx):
        if idx == self.len - 1:
            return 0
        if idx >= self.len:
            return self.max_int
        if self.cache[idx] != None:
            return self.cache[idx]
        ret = self.max_int
        for next_idx in range(idx + 1, idx + self.nums[idx] + 1):
            if next_idx >= self.len:
                break
            ret = min(ret, self.dp(next_idx))
        if ret != self.max_int:
            ret += 1
        self.cache[idx] = ret
        return ret


class Solution:
    def jump(self, nums):
        th = TH(nums)
        return th.dp(0)