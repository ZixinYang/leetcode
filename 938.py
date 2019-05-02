'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
'''

# Tags: Tree Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        ret = 0
        stack = []
        cur = root
        while 1:
            if cur:
                if cur.val>=L and cur.val<=R:
                    ret+=cur.val
                stack.append(cur)
                if cur.val<L:
                    cur.left = None
                cur = cur.left
            else:
                if not stack:
                    break
                cur = stack.pop()
                if cur.val>R:
                    while stack:
                        cur = stack.pop()
                cur = cur.right
        return ret