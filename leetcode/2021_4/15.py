from collections import defaultdict


class Solution:
    def threeSum(self, nums):
        nums_len = len(nums)
        nums.sort()
        # print(nums)
        n_s, n_e, z_s, z_e, p_s, p_e = 0, 0, 0, 0, 0, 0
        n_num, z_num, p_num = 0, 0, 0
        for idx, n in enumerate(nums):
            if n < 0:
                n_num += 1
            elif n == 0:
                z_num += 1
            else:
                p_num += 1
        if n_num == 0:
            n_s, n_e = -1, -1
        else:
            n_s, n_e = 0, n_num - 1
        if z_num == 0:
            z_s, z_e = -1, -1
        else:
            z_s, z_e = n_num, n_num + z_num - 1
        if p_num == 0:
            p_s, p_e = -1, -1
        else:
            p_s, p_e = n_num + z_num, n_num + z_num + p_num - 1

        # print(n_s,n_e,z_s, z_e, p_s, p_e)
        ret = []
        if n_num == 0 or p_num == 0:
            if z_num < 3:
                return ret
            else:
                return [[0] * 3]
        if z_num >= 3:
            ret.append([0, 0, 0])
        n_hash1 = defaultdict(bool)
        n_hash2 = defaultdict(list)
        n_hash_double = defaultdict(bool)

        p_hash1 = defaultdict(bool)
        p_hash2 = defaultdict(list)
        p_hash_double = defaultdict(bool)

        # print("n : ",nums[n_s:n_e+1])
        # print("p : ",nums[p_s:p_e+1])

        for idx in range(n_s, n_e + 1):
            if n_hash1[nums[idx]]:
                n_hash_double[nums[idx]] = True
            else:
                n_hash1[nums[idx]] = True

        for idx in range(p_s, p_e + 1):
            if p_hash1[nums[idx]]:
                p_hash_double[nums[idx]] = True
            else:
                p_hash1[nums[idx]] = True

        if z_num != 0:
            for n in n_hash1.keys():
                val = p_hash1.get(-n, False)
                if val:
                    ret.append([n, 0, -n])

        n_list = list(n_hash1.keys())
        p_list = list(p_hash1.keys())

        for i in range(len(n_list) - 1):
            for j in range(i + 1, len(n_list)):
                n_sum = n_list[i] + n_list[j]
                n_hash2[n_sum].append([n_list[i], n_list[j]])

        for i in range(len(p_list) - 1):
            for j in range(i + 1, len(p_list)):
                p_sum = p_list[i] + p_list[j]
                p_hash2[p_sum].append([p_list[i], p_list[j]])

        #         print("n_hash1 : ", n_hash1)
        #         print("p_hash1 : ", p_hash1)

        #         print("n_hash2 : ", n_hash2)
        #         print("p_hash2 : ", p_hash2)
        #         print("ret : ", ret)

        for n in n_hash1.keys():
            if n_hash1[n]:
                for comb in p_hash2[-n]:
                    ret.append(comb + [n])

        for n in p_hash1.keys():
            if p_hash1[n]:
                for comb in n_hash2[-n]:
                    ret.append(comb + [n])

        for n in n_hash_double.keys():
            if p_hash1[-n * 2]:
                ret.append([n, n, -n * 2])

        for n in p_hash_double.keys():
            if n_hash1[-n * 2]:
                ret.append([n, n, -n * 2])
        return ret