import heapq
class Solution:
    def maxArea(self, height: List[int]) -> int:
        heap = []
        for idx, h in enumerate(height):
            heapq.heappush(heap,(-h,idx))
        max_ret = -1
        h, idx = heapq.heappop(heap)
        min_idx, max_idx = idx, idx
        while heap:
            h, idx = heapq.heappop(heap)
            h *= -1
            dist1 = abs(min_idx - idx)
            dist2 = abs(max_idx - idx)
            max_dist = max(dist1,dist2)
            max_ret = max(max_ret, h*max_dist)
            min_idx = min(min_idx, idx)
            max_idx = max(max_idx, idx)
        return max_ret