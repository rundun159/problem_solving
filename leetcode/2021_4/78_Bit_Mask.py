class Solution:
    def subsets(self, nums):
        n = len(nums)
        ret = []
        for i in range(2 ** n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]
            ret.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return ret
