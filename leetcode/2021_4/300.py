class TH:
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)
        self.cache = [-1 for i in nums]

    def dp(self, idx):
        if idx == self.len:
            return 0
        if self.cache[idx] != -1:
            return self.cache[idx]
        ret = 1
        for i in range(idx + 1, self.len):
            if self.nums[i] > self.nums[idx]:
                ret = max(ret, self.dp(i) + 1)
        self.cache[idx] = ret
        return ret


class Solution:
    def lengthOfLIS(self, nums) -> int:
        th = TH(nums)
        for i in range(th.len):
            th.dp(i)
        ret = -1
        for i in range(th.len):
            ret = max(ret, th.cache[i])
        return ret