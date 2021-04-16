import sys

sys.setrecursionlimit(1000000)


class Solution:
    def searchRange(self, nums, target):
        self.fail = [-1, -1]
        if len(nums) == 0:
            return self.fail
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return self.fail
        self.t = target
        self.nums = nums
        self.len = len(nums)
        first_t_idx, i, j = self.find_target(0, self.len - 1)
        if first_t_idx == -1:
            return self.fail
        if i == j and i != None:
            return [first_t_idx, first_t_idx]
        a_idx = self.find_a_target(i, first_t_idx - 1)
        b_idx = self.find_b_target(first_t_idx + 1, j)
        ret = [-1, -1]
        if a_idx == -1:
            ret[0] = first_t_idx
        else:
            ret[0] = a_idx
        if b_idx == -1:
            ret[1] = first_t_idx
        else:
            ret[1] = b_idx
        return ret

    def find_a_target(self, i, j):
        if i > j:
            return -1
        if i == j:
            if self.nums[i] != self.t:
                return -1
            else:
                return i
        else:
            mid_idx = int((i + j) / 2)
            mid_val = self.nums[mid_idx]
            if mid_val == self.t:
                return self.find_a_target(i, mid_idx)
            else:
                return self.find_a_target(mid_idx + 1, j)

    def find_b_target(self, i, j):
        if i > j:
            return -1
        if i == j:
            if self.nums[i] != self.t:
                return -1
            else:
                return i
        else:
            mid_idx = int((i + j) / 2)
            mid_val = self.nums[mid_idx]
            if mid_val == self.t:
                if (mid_idx + 1) != j:
                    return self.find_b_target(mid_idx, j)
                else:
                    if self.nums[j] == self.t:
                        return j
                    else:
                        return mid_idx
            else:
                return self.find_b_target(i, mid_idx - 1)

    def find_target(self, i, j):
        if i > j:
            return -1, None, None
        if i == j:
            if self.nums[i] != self.t:
                return -1, None, None
            else:
                return i, i, i
        else:
            mid_idx = int((i + j) / 2)
            mid_val = self.nums[mid_idx]
            if mid_val == self.t:
                return mid_idx, i, j
            elif mid_val > self.t:
                return self.find_target(i, mid_idx - 1)
            else:
                return self.find_target(mid_idx + 1, j)
