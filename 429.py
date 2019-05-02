'''
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''

# Tags: Tree Traversal (Level Order)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        cur = root
        queue = [[cur, 0]]
        level = [[cur.val]]

        while queue:
            cur, l = queue.pop(0)
            l += 1
            for child in cur.children:
                queue.append([child, l])
                if len(level) < l + 1: level.append([])
                level[l].append(child.val)
        return level