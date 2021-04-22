class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        cache = [[False for i in range(s_len)] for j in range(s_len)]

        x, y = 0, 0
        max_len = y - x + 1

        for i in range(s_len):
            cache[i][i] = True

        for i in range(s_len - 1):
            if s[i] == s[i + 1]:
                cache[i][i + 1] = True
                max_len = 2
                x, y = i, i + 1
        found = False
        for l in range(3, s_len + 1):
            for s_idx in range(s_len):
                e_idx = s_idx + l - 1
                if e_idx >= s_len:
                    continue
                if s[s_idx] == s[e_idx] and cache[s_idx + 1][e_idx - 1]:
                    cache[s_idx][e_idx] = True
                    if max_len < l:
                        y, x = e_idx, s_idx
                        max_len = l
                else:
                    cache[s_idx][e_idx] = False
        return s[x:y + 1]