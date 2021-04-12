from collections import defaultdict
import heapq
class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k: int) :
        dict = defaultdict(int)
        for n in nums:
            if not dict[n]:
                dict[n] = 1
            else:
                dict[n] += 1
        heap = []
        for key, value in dict.items():
            heapq.heappush(heap, (-value, key))
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret

sol = Solution()
print(sol.topKFrequent( [1,1,1,2,2,3], 2))