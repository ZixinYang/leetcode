'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Note: Bonus points if you could solve it both recursively and iteratively.
'''

# Tags: Tree Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Tags: Recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(T1, T2):
            if T1==None and T2==None: return True
            if T1==None or T2==None: return False
            return (T1.val==T2.val) and isMirror(T1.left, T2.right) and isMirror(T1.right, T2.left)
        return isMirror(root, root)

# Tags: Iteration

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        cur = root
        stack = []
        value1 = []
        while 1:
            if cur:
                stack.append(cur)
                value1.append(cur.val)
                cur = cur.left
            else:
                if not stack:
                    break
                cur = stack.pop()
                cur = cur.right
                if cur:
                    value1.append(None)

        cur = root
        stack = []
        value2 = []
        while 1:
            if cur:
                stack.append(cur)
                value2.append(cur.val)
                cur = cur.right
            else:
                if not stack:
                    break
                cur = stack.pop()
                cur = cur.left
                if cur:
                    value2.append(None)

        return value1 == value2

