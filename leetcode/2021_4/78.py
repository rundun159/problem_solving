class Solution:
    def subsets(self, nums):
        self.nums = nums
        self.len = len(self.nums)
        self.ret=[[]]
        for remain in range(1, self.len+1):
            self.f(-1, remain, [])
        return self.ret
    def f(self, prev_idx, remain, stack):
        if remain == 0:
            self.ret.append(list(stack))
            return
        if prev_idx >= self.len:
            return
        if (self.len - prev_idx -1) < remain:
            return
        for next_idx in range(prev_idx+1, self.len):
            if self.len - next_idx -1 < remain-1:
                return
            stack.append(self.nums[next_idx])
            self.f(next_idx, remain -1, stack)
            stack.pop()
        return