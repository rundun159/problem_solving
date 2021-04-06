class TH:
    def __init__(self, s):
        self.given_str = s
        self.len = len(s)

    def do_bfs(self, k:int , idx_s:int):
        ret = ''
        pos = idx_s
        while pos != self.len:
            if self.given_str[pos] >='a' and self.given_str[pos] <='z':
                ret +=  self.given_str[pos]
                pos += 1
            elif self.given_str[pos] == ']':
                return [ret * k, pos]
            else:
                bracket_idx = None
                for j in range(pos+1,pos+4):
                    if self.given_str[j] == '[':
                        bracket_idx = j
                        break
                next_k = int(self.given_str[pos:bracket_idx])
                small_ret = self.do_bfs(next_k, bracket_idx+1)
                ret += small_ret[0]
                pos = small_ret[1] + 1
        return [ret, pos]
class Solution:
    def decodeString(self, s: str) -> str:
        th = TH(s)
        return th.do_bfs(1,0)[0]

sol = Solution()
print(sol.decodeString("3[a2[c]]"))