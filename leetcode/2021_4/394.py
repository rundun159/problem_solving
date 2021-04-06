class TH:
    def __init__(self, s):
        self.given_str = s
        self.len = len(s)
        self.ret=''
    def main_add(self):
        pos = 0
        while pos != self.len:
            if self.given_str[pos] >='a' and self.given_str[pos] <='z':
                self.ret += self.given_str[pos]
                pos += 1
            else:
                bracket = None
                for j in range(pos+1,pos+4):
                    if self.given_str[j] == '[':
                        bracket = j
                        break
                k = int(self.given_str[pos:bracket])
                small_add_ret, idx_e = self.small_add(k, bracket+1)
                self.ret += small_add_ret
                pos = idx_e + 1
        return self.ret
    def small_add(self,k, idx_s) :
        ret=''
        pos = idx_s
        while pos != self.len:
            if self.given_str[pos] >='a' and self.given_str[pos] <='z':
                ret +=  self.given_str[pos]
                pos += 1
            elif self.given_str[pos] == ']':
                return ret * k, pos
            else:
                bracket = None
                for j in range(pos+1,pos+4):
                    if self.given_str[j] == '[':
                        bracket = j
                        break
                next_k = int(self.given_str[pos:bracket])
                small_add_ret, idx_e = self.small_add(next_k, bracket+1)
                ret += small_add_ret
                pos = idx_e + 1
#    return str, idx
class Solution:
    def decodeString(self, s: str) -> str:
        th = TH(s)
        return th.main_add()
#
# sol = Solution()
# sol.decodeString("3[a2[c]]")