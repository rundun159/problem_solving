class Solution:
    def generateParenthesis(self, n: int):
        self.ret= []
        self.matrix = [[False for i in range(2)] for j in range(n)]
        self.stack = []
        self.cnt = 0
        self.max = n *2
        self.n = n

        self.matrix[0][0] = True
        self.stack.append('(')
        self.cnt += 1

        self.matrix[0][1] = True
        self.stack.append(')')
        self.cnt += 1
        self.dfs(0,1)
        self.cnt -= 1
        self.stack.pop()
        self.matrix[0][1] = False

        if n > 1:
            self.matrix[1][0] = True
            self.stack.append('(')
            self.cnt += 1
            self.dfs(1,0)
            self.cnt -= 1
            self.stack.pop()
            self.matrix[1][0] = False
        return self.ret

    def dfs(self,i,j):
        if self.cnt == self.max:
            now_str = ''
            for c in self.stack:
                now_str+=c
            self.ret.append(now_str)
            return
        if j == 0:
            self.matrix[i][1] = True
            self.stack.append(')')
            self.cnt += 1
            self.dfs(i, 1)
            self.cnt -= 1
            self.stack.pop()
            self.matrix[i][1] = False

            if i+1 < self.n:
                self.matrix[i+1][0] = True
                self.stack.append('(')
                self.cnt += 1
                self.dfs(i+1, 0)
                self.cnt -= 1
                self.stack.pop()
                self.matrix[i+1][0] = False
        else:
            # if i-1 >=0 and not self.matrix[i-1][1]:
            for next_i in reversed(range(i)):
                if not self.matrix[next_i][1]:
                    self.matrix[next_i][1] = True
                    self.stack.append(')')
                    self.cnt += 1
                    self.dfs(next_i, 1)
                    self.cnt -= 1
                    self.stack.pop()
                    self.matrix[next_i][1] = False
                    break
            for next_i in range(i+1, self.n):
                if not self.matrix[next_i][0]:
                    self.matrix[next_i][0] = True
                    self.stack.append('(')
                    self.cnt += 1
                    self.dfs(next_i, 0)
                    self.cnt -= 1
                    self.stack.pop()
                    self.matrix[next_i][0] = False
                    return

# sol = Solution()
# print(sol.generateParenthesis(3))