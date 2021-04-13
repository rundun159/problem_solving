from collections import defaultdict

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        org_head = head
        org_dict = defaultdict(int)
        org_list = [head]
        org_idx = 1
        org_dict[org_head] = org_idx

        new_head = Node(head.val)
        new_dict = defaultdict(int)
        new_list = [new_head]
        new_idx = 1
        new_dict[new_head] = new_idx

        org_now = org_head.next
        new_prev = new_head
        while org_now:
            org_list.append(org_now)
            org_idx += 1
            org_dict[org_now] = org_idx

            new_now = Node(org_now.val)
            new_prev.next = new_now
            new_list.append(new_now)
            new_idx += 1
            new_dict[new_now] = new_idx
            new_prev = new_now

            org_now = org_now.next

        org_random = [None for i in org_list]
        new_random = [None for i in new_list]

        for idx, n in enumerate(org_list):
            # if n.random:
            #     print(idx, n.val, n.random.val, org_dict[n.random])
            # else:
            #     print(idx, n.val)
            if org_dict[n.random]:
                r_idx = org_dict[n.random] -1
                new_list[idx].random = new_list[r_idx]
        return new_list[0]
# head = Node(4)
# sol = Solution()
# sol.copyRandomList(head)