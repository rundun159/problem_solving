from collections import defaultdict
ops = ['*','+','-']
op_orders = []
ops_bool = [False for i in range(3)]
stack = []
def make_op_orders(cnt, stack):
    if cnt == 3:
        op_orders.append(stack[:])
    for i in range(3):
        if not ops_bool[i]:
            ops_bool[i] = True
            stack.append(ops[i])
            make_op_orders(cnt + 1, stack)
            ops_bool[i] = False
            stack.pop()
make_op_orders(0, stack)
def op_ret(op1,op2,op):
    if op == '*':
        return op1*op2
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1-op2
def ret_val(final_list, op_order):
    now_list = final_list[:]
    stack = []
    for op in op_order:
        map_bool = defaultdict(bool)
        for idx, c in enumerate(now_list):
            v = map_bool.get(idx,False)
            if not v:
                if c == op:
                    prev = stack.pop()
                    post = now_list[idx+1]
                    map_bool[idx+1] = True
                    val = op_ret(prev,post,c)
                    stack.append(val)
                else:
                    stack.append(c)
        now_list = stack
        stack = []
    return abs(now_list[0])
def solution(expression):
    final_list = []
    now_idx = 0
    prev_op = -1
    for idx, c in enumerate(expression):
        if c in ops:
            final_list.append(int(expression[prev_op + 1:idx]))
            final_list.append(c)
            prev_op = idx
    final_list.append(int(expression[prev_op + 1:]))
    ret = ret_val(final_list,op_orders[0])
    for op_order in op_orders[1:]:
        ret = max(ret, ret_val(final_list,op_order))
    return ret
