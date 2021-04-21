import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_val = -100000
        self.max_val = 100000
        self.min_heap = []
        self.max_heap = []
        self.min_heap_len = 0
        self.max_heap_len = 0
        self.start = True

    def add_min_h(self, num):
        heapq.heappush(self.min_heap, (-num, num))
        self.min_heap_len += 1

    def add_max_h(self, num):
        heapq.heappush(self.max_heap, num)
        self.max_heap_len += 1

    def pop_min_h(self):
        _, min_top = heapq.heappop(self.min_heap)
        self.min_heap_len -= 1
        return min_top

    def pop_max_h(self):
        max_top = heapq.heappop(self.max_heap)
        self.max_heap_len -= 1
        return max_top

    def is_min_large(self):
        return self.min_heap_len > self.max_heap_len

    def is_max_large(self):
        return self.min_heap_len < self.max_heap_len

    def addNum(self, num: int) -> None:
        if self.min_heap_len < self.max_heap_len:
            max_top = self.max_heap[0]
            if num >= max_top:
                max_top = self.pop_max_h()
                self.add_min_h(max_top)
                self.add_max_h(num)
            else:
                self.add_min_h(num)
        elif self.min_heap_len > self.max_heap_len:
            min_top = self.min_heap[0][1]
            if num < min_top:
                min_top = self.pop_min_h()
                self.add_max_h(min_top)
                self.add_min_h(num)
            else:
                self.add_max_h(num)
        else:
            if not self.start:
                max_top = self.max_heap[0]
                if num <= max_top:
                    self.add_min_h(num)
                else:
                    self.add_max_h(num)
            else:
                self.start = False
                self.add_max_h(num)
        # print("After addNum")
        # print("min : ", self.min_heap)
        # print("max : ", self.max_heap)
        # print("Len : ", self.min_heap_len, self.max_heap_len)

    def findMedian(self) -> float:
        # print("In find")
        # print("In find : ", self.min_heap, self.max_heap)
        # print("Len : ", self.min_heap_len, self.max_heap_len)
        if self.min_heap_len > self.max_heap_len:
            return self.min_heap[0][1]
        elif self.min_heap_len < self.max_heap_len:
            return self.max_heap[0]
        elif self.min_heap_len == self.max_heap_len:
            mid = self.min_heap[0][1]
            mid += self.max_heap[0]
            return mid / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()