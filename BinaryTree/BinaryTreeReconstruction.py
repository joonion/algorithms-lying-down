# Definition for a binary tree node.
class TreeNode:
    def __init__(self, item = 0, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

from typing import List 

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        else:
            root, pos = preorder[0], inorder.index(preorder[0])
            left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
            right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])
            return TreeNode(root, left, right)

def preorder(root):
    if root is not None:
        print(root.item, end = " ")
        preorder(root.left)
        preorder(root.right)

s = Solution()
pre = [3,9,20,15,7] 
ino = [9,3,15,20,7]
root = s.buildTree(pre, ino)
preorder(root)
