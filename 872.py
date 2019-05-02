'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:

Both of the given trees will have between 1 and 100 nodes.
'''

# Tags: Tree Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def iterative(root):
            leaf = []
            stack = []
            while 1:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    if not stack:
                        break
                    else:
                        root = stack.pop()
                        if not root.left and not root.right:
                            leaf.append(root.val)
                        root = root.right
            return leaf

        return iterative(root1 )= =iterative(root2)