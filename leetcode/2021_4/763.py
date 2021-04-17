from collections import defaultdict, deque


class TH:
    def __init__(self, S):
        self.S = S
        self.len = len(S)
        self.bool_list = [False for i in range(26)]
        self.dict = defaultdict(list)
        self.alpha_list = [str(i) for i in range(ord('a'), ord('z') + 1)]
        for idx, c in enumerate(S):
            self.dict[c].append(idx)

    def greedy(self):
        pass
        last = {c: i for i, c in enumerate(self.S)}
        self.greedy_ret = []
        anchor = j = 0
        for i, c in enumerate(self.S):
            j = max(j, last[c])
            if i == j:
                self.greedy_ret.append(i - anchor + 1)
                anchor = i + 1

    def use_bfs(self):
        q = deque()
        self.part_num = 0
        self.ret = []
        for idx, a in enumerate(S):
            a_a_idx = ord(a) - ord('a')
            # print(a, a_a_idx)
            if not self.bool_list[a_a_idx]:
                self.part_num += 1
                self.bool_list[a_a_idx] = True
                q.append(a)
                if len(self.dict[a]) == 1:
                    q.popleft()
                    self.ret.append(1)
                    continue
                init_bnd = [self.dict[a][0], self.dict[a][-1]]
                while q:
                    front_a = q.popleft()
                    if len(self.dict[front_a]) <= 1:
                        continue
                    now_bnd = [self.dict[front_a][0], self.dict[front_a][-1]]
                    init_bnd = [min(init_bnd[0], now_bnd[0]), max(init_bnd[1], now_bnd[1])]
                    for c in self.S[now_bnd[0]: now_bnd[1]]:
                        if a != c:
                            c_a_idx = ord(c) - ord('a')
                            if not self.bool_list[c_a_idx]:
                                self.bool_list[c_a_idx] = True
                                q.append(c)
                # print(init_bnd)
                self.ret.append(init_bnd[1] - init_bnd[0] + 1)


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        th = TH(S)
        th.greedy()
        return th.greedy_ret