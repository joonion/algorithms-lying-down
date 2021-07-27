# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        achilles = tortoise = hare = head
        while hare != None and hare.next != None:
            hare = hare.next.next
            achilles, tortoise = tortoise, tortoise.next
        root = TreeNode(tortoise.val)
        if achilles != tortoise:
            achilles.next = None
            root.left = self.sortedListToBST(head)
        if tortoise.next != None:
            root.right = self.sortedListToBST(tortoise.next)
        return root