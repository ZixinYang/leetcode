'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Tags: Tree Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stack = []
        cur = root
        mini = float('-inf')
        while 1:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                if not stack:
                    break
                cur = stack.pop()
                if cur.val <= mini:
                    return False
                mini = cur.val
                cur = cur.right
        return True