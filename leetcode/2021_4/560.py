from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k) -> int:
        sum_dict = defaultdict(int)
        sum_nums = 0
        sum_dict[0] = 1
        ret = 0
        for n in nums:
            sum_nums += n
            prev = sum_nums - k
            tmp = sum_dict.get(prev,0)
            ret += tmp
            sum_dict[sum_nums] += 1
        return ret