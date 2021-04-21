from collections import defaultdict


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums, idx, remain):
            if remain == 0:
                return True
            if remain < 0 or idx < 0:
                return False
            ret = (dfs(nums, idx - 1, remain - nums[idx])) or dfs(nums, idx - 1, remain)
            return ret

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        remain = total_sum // 2
        nums_len = len(nums)
        return dfs(tuple(nums), nums_len - 1, remain)
