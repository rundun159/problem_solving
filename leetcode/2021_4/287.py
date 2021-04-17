class Solution:
    def findDuplicate(self, nums) :
        bool_list = [False for i in range(len(nums))]
        for n in nums:
            if bool_list[n]:
                return n
            else:
                bool_list[n] = True