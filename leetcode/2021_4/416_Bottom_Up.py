from collections import defaultdict

class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        remain = total_sum // 2
        self.len = len(nums)
        self.nums = sorted(nums)
        max_num = max(nums[-1],remain)
        self.cache = [[False for i in range(max_num+1)] for j in range(self.len)]
        return self.dp_bottom_up(remain)
    def dp_bottom_up(self, remain):
        self.cache[0][0] = True
        self.cache[0][self.nums[0]] = True
        for idx, val in enumerate(self.nums[1:]):
            idx += 1
            for j in range(remain +1):
                if j < val:
                    self.cache[idx][j] = self.cache[idx-1][j]
                else:
                    self.cache[idx][j] = self.cache[idx-1][j] or self.cache[idx-1][j-val]
        return self.cache[self.len-1][remain]
    def dp(self,remain, idx):
        if remain == 0:
            return True
        if remain < 0 or idx >= self.len:
            return False
        if self.cache[remain][idx] != None:
            return self.cache[remain][idx]
        ret1 = self.dp(remain, idx +1)
        if ret1:
            return ret1
        if remain - self.nums[idx]>=0:
            ret2 = self.dp(remain - self.nums[idx], idx +1)
            if ret2:
                return ret2
        self.cache[remain][idx] = False
        return False