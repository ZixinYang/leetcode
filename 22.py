'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

# Tags: Recursion

class Solution:
    def generator(self, pair, nl, nr):
        if nl == 0 and nr == 0:
            self.ret.append(pair)
        if nl > 0:
            self.generator(pair + '(', nl - 1, nr + 1)
        if nr > 0:
            self.generator(pair + ')', nl, nr - 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.ret = []
        self.generator('', n, 0)
        return self.ret