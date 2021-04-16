class Solution:
    def partition(self, s):
        total_len = len(s)
        ret = []

        def ckeck_pal(word):
            word_len = len(word)
            mid_idx = int(word_len / 2)
            for i in range(mid_idx):
                end_idx = word_len - i - 1
                if word[i] != word[end_idx]:
                    return False
            return True

        def backtrack(remain, comb, start):
            if remain == 0:
                ret.append(list(comb))
            new_cand = ''
            for end in range(start, total_len):
                new_cand += s[end]
                if ckeck_pal(new_cand):
                    comb.append(new_cand)
                    backtrack(remain - len(new_cand), comb, end + 1)
                    comb.pop()

        backtrack(total_len, [], 0)
        return ret
