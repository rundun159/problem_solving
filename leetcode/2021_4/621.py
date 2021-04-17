from collections import defaultdict
import heapq


class Solution:
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)
        self.org_task = tasks
        max_list = []
        task_dict = defaultdict(int)
        for t in tasks:
            task_dict[t] += 1
        for key, item in task_dict.items():
            heapq.heappush(max_list, (-item, key))

        ret = 0

        while (len(max_list) - 1) > n:
            left = len(max_list) - 1
            top_list = []
            for i in range(n + 1):
                top_list.append(heapq.heappop(max_list))
            m = top_list[n][0]
            ret += (n + 1) * (m * -1)
            for i in range(n):
                next_item = top_list[i][0] - m
                if next_item:
                    heapq.heappush(max_list, (top_list[i][0] - m, top_list[i][1]))

        x = max_list[0][0]
        cnt = 0
        for v, k in max_list[1:]:
            if x == v:
                cnt += 1
            else:
                break

        ret += (n + 1) * (-x - 1) + 1 + cnt
        return ret