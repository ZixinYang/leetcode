'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example:

[
  [3],
  [9,20],
  [15,7]
]

'''

# Tags: Tree Traversal (Level Order)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        cur = root
        queue = [[cur, 0]]
        level = [[cur.val]]
        while queue:
            cur, l = queue.pop(0)
            if cur.left or cur.right:
                l+=1
                if cur.left:
                    queue.append([cur.left, l])
                    if len(level)<l+1: level.append([])
                    level[l].append(cur.left.val)
                if cur.right:
                    queue.append([cur.right, l])
                    if len(level)<l+1: level.append([])
                    level[l].append(cur.right.val)
        return level