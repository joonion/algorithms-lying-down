# Floyd's Tortoise-Hare Algorithm for Cycle Detection
# LeetCode Problem 141: Linked List Cycle

class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> ListNode:
        hare = tortoise = head
        while hare != None and tortoise != None:
            if hare.next == None: 
                return False
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False

items = [3, 2, 0, -4]
links = [1, 2, 3, 1]
nodes = [ListNode(i) for i in items]
for node, link in zip(nodes, links):
    node.next = nodes[link]

for node in nodes:
    print(node.item, end=": ")
    if node.next != None: 
        print(node.next.item)
    else:
        print("null")

s = Solution()
print(s.hasCycle(nodes[0]))


