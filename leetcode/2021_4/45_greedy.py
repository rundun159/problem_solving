class Solution:
    def jump(self, nums):
        self.len = len(nums)
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(self.len -1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps