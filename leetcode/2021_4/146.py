class Node:
    def __init__(self, key=None, value=None, prev_Node=None, next_Node=None):
        self.key = key
        self.val = value
        self.prev = prev_Node
        self.next = next_Node
        if self.prev:
            self.prev.next = self
        if self.next:
            self.next.prev = self


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_num = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def add_node(self, key, value):
        if self.node_num == self.capacity:
            self.remove_lru_node()
        new_node = Node(key, value, self.head, self.head.next)
        self.cache[key] = new_node
        self.node_num += 1

    def pop_node(self, node):
        prev_N = node.prev
        next_N = node.next
        prev_N.next = next_N
        next_N.prev = prev_N

    def put_to_front(self, node):
        head1, head2 = self.head, self.head.next
        head1.next = node
        head2.prev = node
        node.prev = head1
        node.next = head2

    def remove_lru_node(self):
        lru_node = self.tail.prev
        self.pop_node(lru_node)
        del self.cache[lru_node.key]
        self.node_num -= 1

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self.pop_node(node)
        self.put_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if not node:
            self.add_node(key, value)
        else:
            node.val = value
            self.pop_node(node)
            self.put_to_front(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)