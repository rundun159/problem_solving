class Solution:
    def permute(self, nums):
        self.total_len = len(nums)
        self.ret = []
        self.nums = nums
        stack = []
        bool_list = [False for i in nums]
        self.bf(stack, bool_list)
        return self.ret
    def bf(self, stack, bool_list):
        if len(stack) == self.total_len:
            self.ret.append([i for i in stack])
            return
        for idx, v in enumerate(self.nums):
            if not bool_list[idx]:
                bool_list[idx] = True
                stack.append(v)
                self.bf(stack ,bool_list)
                bool_list[idx] = False
                stack.pop()
        return
