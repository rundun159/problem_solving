import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda k : k[0])
        heap = []
        max_len = 0
        for meet in intervals:
            meet_start, meet_end = meet
            if not heap:
                heap.append((meet_end,meet_start))
            else:
                while heap:
                    top_end = heap[0][0]
                    if meet_start >= top_end:
                        heapq.heappop(heap)
                    else:
                        break
                heapq.heappush(heap, (meet_end,meet_start))
            max_len = max(max_len, len(heap))
        return max_len