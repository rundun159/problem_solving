class Robot:
    def __init__(self,instructions):
        self.inst_len = len(instructions)
        self.ways=4
        self.step_forward=[[0,1],[1,0],[0,-1],[-1,0]]
        self.dir = 0
        self.pos = [0,0]
        self.inst_arr=[]
        for i in instructions:
            if i == 'G':
                self.inst_arr.append(0)
            elif i == 'L':
                self.inst_arr.append(1)
            elif i == 'R':
                self.inst_arr.append(2)
    def do_inst(self):
        # print("in do function")
        for i in self.inst_arr:
            if i==0:
                self.pos[0] += self.step_forward[self.dir][0]
                self.pos[1] += self.step_forward[self.dir][1]
            elif i==1:
                self.dir = (self.dir+3)%self.ways
            elif i==2:
                self.dir = (self.dir+1)%self.ways
            # self.print_robot()

    def print_robot(self):
        print(self.dir, self.pos)
class Solution(object):
    def isRobotBounded(self, instructions):
        robot = Robot(instructions)
        # print(robot.inst_arr)
        robot.do_inst()
        if robot.dir==0:
            print(0)
            # robot.print_robot()
            if robot.pos != [0,0]:
                return False
            else:
                return True
        elif robot.dir==2:
            robot.do_inst()
            # print(1)
            # robot.print_robot()
            if robot.pos != [0,0]:
                return False
            else:
                return True
        else:
            # print(2)
            for i in range(3):
                robot.do_inst()
                # robot.print_robot()
            if robot.pos != [0,0]:
                return False
            else:
                return True


inst1 = "GGLLGG"
inst2 = "GGLGLGRG"
sol = Solution()
print(sol.isRobotBounded(inst1))
print(sol.isRobotBounded(inst2))