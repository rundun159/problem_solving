class Solution:
    def maxProduct(self, nums):
        self.min_int = -1 * (1 << 31) - 1
        zero_found = False
        part_list = []
        new_list = []
        for n in nums:
            if n == 0:
                part_list.append(new_list)
                new_list = []
                zero_found = True
            else:
                new_list.append(n)
        part_list.append(new_list)
        ret = self.min_int
        if zero_found:
            ret = 0
        print(part_list)
        for part in part_list:
            print(part)
            ret = max(ret, self.ret_max(part))
        return ret

    def ret_max(self, part):
        if not part:
            return self.min_int
        mv_list = []
        now = 1
        v_cnt = 0
        for p in part:
            if p < 0:
                v_cnt += 1
                mv_list.append(now)
                mv_list.append(p)
                now = 1
            else:
                now *= p

        mv_list.append(now)
        q = int(v_cnt % 2)
        ret = 1
        for m in mv_list:
            ret *= m
        if v_cnt == 0 or q == 0:
            return ret
        elif v_cnt == 1:
            if len(part) == 1:
                return part[0]
            elif len(part) == 2:
                max_val = max(part[0], part[1])
                return max_val
            else:
                return max(mv_list[0], mv_list[-1])
        else:
            mv1 = mv_list[0] * mv_list[1]
            mv2 = mv_list[-2] * mv_list[-1]
            max_mv = max(mv1, mv2)
            return int(ret / max_mv)