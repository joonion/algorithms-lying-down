# Floyd's Tortoise-Hare Algorithm for Cycle Detection
#   Finding the starting position of the cycle
# LeetCode Problem 142: Linked List Cycle II

class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Phase 1: Detecting the cycle
        hare = tortoise = head
        while hare != None and tortoise != None:
            if hare.next == None: 
                return None
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                # Phase 2: Finding the starting position
                hare = head
                while hare != tortoise: 
                    hare = hare.next
                    tortoise = tortoise.next
                return hare
        return None

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
print(s.detectCycle(nodes[0]).item)

