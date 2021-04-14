from collections import defaultdict
DEBUG = False
DIR = [[1,0], [-1,0], [0, 1], [0, -1]]
class Solution:
    def exist(self, board, word) :
        board_dict = defaultdict(int)
        word_dict = defaultdict(int)
        for l in board:
            for c in l:
                board_dict[c] += 1
        for c in word:
            word_dict[c] += 1
        for k, item in board_dict.items():
            word_dict[k] -= item
        for k, item in word_dict.items():
            if item > 0:
                return False
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.word = word
        self.len = len(word)
        self.total = self.m * self.n
        if self.len > self.total:
            return False
        idx_dict = defaultdict(list)
        for idx, c in enumerate(word):
            idx_dict[c].append(idx)
        start_c = word[0]
        start_list = []
        self.edge_map = [[[] for i in range(self.n)] for j in range(self.m)]
        if DEBUG:
            print(self.edge_map)
        for row_idx, row in enumerate(board):
            for col_idx, c in enumerate(row):
                if c == start_c:
                    start_list.append((row_idx,col_idx))
                idx_list = idx_dict[c]
                for idx in idx_list:
                    if idx >= (self.len -1):
                        continue
                    next_idx = idx+1
                    next_c = word[next_idx]
                    idx_list2 = idx_dict[next_c]
                    for d in DIR:
                        r, c= row_idx + d[0], col_idx + d[1]
                        if DEBUG:
                            print(row_idx, r, col_idx, c)
                        if r<0 or r>= self.m:
                            continue
                        if c<0 or c>= self.n:
                            continue
                        if board[r][c] == next_c:
                            self.edge_map[row_idx][col_idx].append((r,c))
        if DEBUG:
            for i in self.edge_map:
                print(i)
            # print(self.edge_map)


        self.gone = [[False for i in range(self.n)] for j in range(self.m)]

        for pos in start_list:
            r, c = pos
            self.gone[r][c] = True
            if self.dfs(0,r,c):
                return True
            self.gone[r][c] = False

        return False


    def dfs(self, idx, r, c):
        if DEBUG:
            print(idx, r, c)
        if idx == (self.len-1 ):
            return True
        for next_pos in self.edge_map[r][c]:
            next_r, next_c = next_pos
            if not self.gone[next_r][next_c]:
                if self.word[idx+1] == self.board[next_r][next_c]:
                    self.gone[next_r][next_c] = True
                    if self.dfs(idx+1, next_r,next_c):
                        return True
                    self.gone[next_r][next_c] = False
        return False

if DEBUG:
    sol = Solution()
    print(sol.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaab"))

