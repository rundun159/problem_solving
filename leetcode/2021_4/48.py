
DEBUG = False
class Solution:
    def __init__(self):
        self.DIR1 = [[0,1],[1,0],[0,-1],[-1,0]]
        self.DIR2 = [[0, 0], [0, 1], [1, 1], [1, 0]]
    def rotate(self, matrix) -> None:
        len(matrix)
        n = len(matrix[0])
        m = int(n/2)
        if n%2 == 0:
            for i in range(1, m+1):
                s_list = [ [m-i,m-i] for j in range(4)]
                self.len = 2*i -1
                for j, dir in enumerate(self.DIR2):
                    s_list[j] = [s_list[j][0] + dir[0] * self.len,s_list[j][1] + dir[1] * self.len ]
                if DEBUG:
                    print("s_list : ")
                    print(s_list)
                for j in range(self.len):
                    now_list = [[i[0],i[1]] for i in s_list]
                    for z, dir in enumerate(self.DIR1):
                        now_list[z] = [now_list[z][0] + j * dir[0] ,now_list[z][1] + j * dir[1] ]
                    if DEBUG:
                        print("now_list : ")
                        print(now_list)
                    v_list = [None for q in range(4)]
                    for idx, pos in enumerate(now_list):
                        v_list[idx] = matrix[pos[0]][pos[1]]
                    if DEBUG:
                        print(v_list)
                    for idx, pos in enumerate(now_list):
                        matrix[pos[0]][pos[1]] = v_list[(idx+3)%4]
        else:
            for i in range(1, m+1):
                s_list = [ [m-i,m-i] for j in range(4)]
                self.len = 2*i
                for j, dir in enumerate(self.DIR2):
                    s_list[j] = [s_list[j][0] + dir[0] * self.len,s_list[j][1] + dir[1] * self.len ]
                if DEBUG:
                    print("s_list : ")
                    print(s_list)
                for j in range(self.len):
                    now_list = [[i[0],i[1]] for i in s_list]
                    for z, dir in enumerate(self.DIR1):
                        now_list[z] = [now_list[z][0] + j * dir[0] ,now_list[z][1] + j * dir[1] ]
                    if DEBUG:
                        print("now_list : ")
                        print(now_list)
                    v_list = [None for q in range(4)]
                    for idx, pos in enumerate(now_list):
                        v_list[idx] = matrix[pos[0]][pos[1]]
                    if DEBUG:
                        print(v_list)
                    for idx, pos in enumerate(now_list):
                        matrix[pos[0]][pos[1]] = v_list[(idx+3)%4]
#         print(matrix)
# sol = Solution()
# sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
# sol.rotate([[1,2,3],[4,5,6],[7,8,9]])