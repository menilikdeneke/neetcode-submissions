"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None}
        cur = head
        while cur != None:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur != None:
            copy = oldToCopy[cur]
            copy.random = oldToCopy[cur.random]
            copy.next = oldToCopy[cur.next]
            cur = cur.next

        return oldToCopy[head]