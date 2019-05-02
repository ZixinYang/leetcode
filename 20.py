'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true
'''

# Tags: Hash Table, Stack

class Solution:
    def isValid(self, s: str) -> bool:
        MAP = {'(':')', '{':'}', '[':']'}
        stack = []
        for x in s:
            if x=='(' or x=='{' or x=='[':
                stack.append(x)
            else:
                if not stack: return False
                y = stack.pop()
                if MAP[y]!=x: return False
        if not stack: return True
        else: return False