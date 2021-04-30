def solution(numbers, hand):
    left = False
    if hand == "left":
        left = True
    answer = ''
    now_left_pos = [3,0]
    now_right_pos = [3,2]
    num_pos =[
        [3,1],[0,0],[0,1],[0,2],
        [1,0],[1,1],[1,2],
        [2,0],[2,1],[2,2]
    ]
    def get_dist(pos1,pos2):
        ret = 0
        ret += abs(pos1[0]-pos2[0])
        ret += abs(pos1[1]-pos2[1])
        return ret
    left_num = [1,4,7]
    right_num = [3,6,9]
    mid_num = [0,2,5,8]
    for n in numbers:
        n_pos = num_pos[n]
        if n in left_num:
            answer += 'L'
            now_left_pos = n_pos
        elif n in right_num:
            answer += 'R'
            now_right_pos = n_pos
        else:
            l_dist = get_dist(n_pos, now_left_pos)
            r_dist = get_dist(n_pos, now_right_pos)
            if l_dist < r_dist:
                answer+='L'
                now_left_pos = n_pos
            elif l_dist > r_dist:
                answer += 'R'
                now_right_pos = n_pos
            else:
                if left:
                    answer+='L'
                    now_left_pos = n_pos
                else:
                    answer += 'R'
                    now_right_pos = n_pos
    return answer