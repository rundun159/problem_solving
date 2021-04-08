import heapq
class Solution:
    def findKthLargest(self, nums , k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap,(-n,n))
        for i in range(k):
            ret = heapq.heappop(heap)
        return ret[1]

# nums = [3,2,1,5,6,4]
# k = 3
#
# sol = Solution()
# print(sol.findKthLargest(nums,k))