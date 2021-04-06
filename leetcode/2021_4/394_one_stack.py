class TH:
    def __init__(self,s):
        self.s = s
        self.len = len(s)
    def do_stack(self):
        self.stack = []
        for c in self.s:
            if c != ']':
                self.stack.append(c)
            else:
                inside = ''
                while self.stack[-1] != '[':
                    inside += self.stack.pop()
                self.stack.pop()
                k = ''
                while len(self.stack) != 0  and (self.stack[-1]>='0' and self.stack[-1]<='9') :
                    k += self.stack.pop()
                k = k[::-1]
                inside = inside * int(k)
                for c in reversed(inside):
                    self.stack.append(c)
        ret = ''
        for c in self.stack:
            ret += c
        return ret
class Solution:
    def decodeString(self, s: str) -> str:
        th = TH(s)
        return th.do_stack()

sol = Solution()
print(sol.decodeString("3[a2[c]]"))