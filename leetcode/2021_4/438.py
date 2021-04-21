# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:

class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []
        self.p_cnt = [0 for i in range(26)]
        for c in p:
            self.p_cnt[ord(c) - ord('a')] += 1
        ret = []
        s_cnt = [0 for i in range(26)]
        self.p_len = len(p)
        self.s_len = len(s)
        start, end = 0, self.p_len - 1
        for c in s[start:end + 1]:
            s_cnt[ord(c) - ord('a')] += 1
        if self.p_cnt == s_cnt:
            ret.append(0)
        for start in range(1, self.s_len - self.p_len + 1):
            prev = start - 1
            new = start + self.p_len - 1
            s_cnt[ord(s[prev]) - ord('a')] -= 1
            s_cnt[ord(s[new]) - ord('a')] += 1
            if self.p_cnt == s_cnt:
                ret.append(start)
        return ret