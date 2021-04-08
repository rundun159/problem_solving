class TH:
    def __init__(self,strs):
        self.strs = strs
        self.nums = len(strs)
        self.matrix1 = [[0 for x in range(26)] for y in range (self.nums)]
        self.org_idx = [ i for i in range(self.nums)]
        for idx, s in enumerate(strs):
            for c in s:
                c_idx = ord(c) - ord('a')
                # print(idx, s, c)
                # print(idx, c_idx)
                self.matrix1[idx][c_idx] += 1
        # print("init")
        # for l in self.matrix1:
        #     print(l)
        # print(self.matrix1)
    def radix_sort(self, idx):
        matrix2 = [[0 for x in range(26)] for y in range (self.nums)]
        org_idx2 = [None for x in range(self.nums)]

        target = [None for x in range( self.nums)]
        for i in range(self.nums):
            target[i]=self.matrix1[i][idx]

        sorted_1 = sorted(range(self.nums), key=lambda k: target[k])
        for i in sorted_1:
            for j in range(26):
                matrix2[i][j] = self.matrix1[sorted_1[i]][j]
            org_idx2[i] = self.org_idx[sorted_1[i]]
        del self.matrix1
        del self.org_idx
        
        self.matrix1 = matrix2
        self.org_idx = org_idx2
        return
    def th_main(self):
        for i in range(26):
            self.radix_sort(i)
        ret = []
        anagram_cnt = 0
        anagram_idx = -1
        prev = [-1]*26
        # print("prev, l")
        for idx, l in enumerate(self.matrix1):
            # print(prev, l)
            if prev != l:
                anagram_cnt += 1
                anagram_idx += 1
                ret.append([])
                ret[anagram_idx].append(self.strs[self.org_idx[idx]])
                prev = l
            else:
                ret[anagram_idx].append(self.strs[self.org_idx[idx]])
        return ret
class Solution:
    def groupAnagrams(self, strs):
        th = TH(strs)
        return th.th_main()

# strs = ["eat","tea","tan","ate","nat","bat"]
# sol = Solution()
# print(sol.groupAnagrams(strs))