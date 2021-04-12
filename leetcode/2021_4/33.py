class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target: int) -> int:
        self.target = target
        self.nums = nums
        self.ret = -1
    def s(self, idx1, idx2):
        if idx2 < idx1:
            return
        len = idx2 - idx1 + 1
        if len < 5:
            for i in range(idx1, idx2+1):
                if self.nums[i] == self.target:
                    self.ret = i
                    return
        mid_idx = int((idx1+idx2)/2)
        x1 = self.nums[idx1]
        x2 = self.nums[mid_idx]
        if x1 == self.target:
            self.ret = idx1
            return
        if x2 == self.target:
            self.ret = mid_idx
            return
        A = [idx1+1, mid_idx-1]
        B = [mid_idx +1 , idx2]
        # print(A,B)
        if x1<x2:
            if self.target < x1:
                self.s(B[0],B[1])
            elif self.target < x2:
                self.s(A[0], A[1])
            else:
                self.s(B[0], B[1])
        else:
            if self.target < x2:
                self.s(A[0], A[1])
            elif self.target < x1:
                self.s(B[0], B[1])
            else:
                self.s(A[0], A[1])
        return

sol = Solution()
nums=[4,5,6,7,0,1,2]
target = 100
sol.search(nums = nums, target = target)
sol.s(0,len(nums)-1)
print(sol.ret)