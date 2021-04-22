class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_list = []
        end_list = []
        for m in intervals:
            start_list.append(m[0])
            end_list.append(m[1])
        start_list.sort()
        end_list.sort()
        max_rooms = 1
        rooms = 1
        start_idx = 0
        end_idx = 0
        for start_idx in range(1,len(intervals)):
            rooms += 1
            while start_list[start_idx] >= end_list[end_idx] and end_idx < start_idx:
                end_idx += 1
                rooms -= 1
            max_rooms = max(max_rooms, rooms)
        return max_rooms