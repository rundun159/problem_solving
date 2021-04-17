class TH:
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)

    def dp(self, idx):
        self.cache = [-1 for i in self.nums]
        if idx >= self.len:
            return 0
        if self.cache[idx] != -1:
            return self.cache[idx]
        ret = self.nums[idx]
        for next_idx in range(idx + 2, self.len):
            ret = max(ret, self.dp(next_idx) + self.nums[idx])
        self.cache[idx] = ret
        return ret

    def top_down_dp(self):
        self.cache2 = [None for i in self.nums + [None]]
        self.cache2[self.len] = 0
        self.cache2[self.len - 1] = self.nums[-1]
        for idx in range(self.len - 2, -1, -1):
            self.cache2[idx] = max(self.cache2[idx + 1], self.cache2[idx + 2] + self.nums[idx])
        return self.cache2[0]

    def optimized_dp(self):
        next_val2 = 0
        next_val = self.nums[self.len - 1]

        for idx in range(self.len - 2, -1, -1):
            current = max(next_val, next_val2 + self.nums[idx])

            next_val2 = next_val
            next_val = current

        return next_val


class Solution:
    def rob(self, nums) :
        th = TH(nums)

        # for i in range(th.len):
        #     th.dp(i)
        # ret = -1
        # for i in th.cache:
        #     ret = max(ret, i)
        # return ret

        # return  th.top_down_dp()

        return th.optimized_dp()