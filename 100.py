'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''

# Tags: Tree Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def iterative(root):
            stack = []
            structure = []
            while 1:
                if root:
                    stack.append(root)
                    structure.append(root.val)
                    root = root.left
                else:
                    if not stack:
                        break
                    else:
                        structure.append(root)
                        if structure[-2:] == [None, None]:
                            structure.pop()
                            structure.pop()
                        root = stack.pop()
                        root = root.right
            return structure

        return iterative(p) == iterative(q)