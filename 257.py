'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
'''

# Tags: Tree Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        stack = []
        paths = []
        path = ""
        while 1:
            if root:
                path = path+"->"+str(root.val)
                stack.append([root,path])
                root = root.left
            else:
                if not stack:
                    break
                else:
                    root, path = stack.pop()
                    if not root.left and not root.right:
                        paths.append(path[2:])
                    root = root.right
        return paths