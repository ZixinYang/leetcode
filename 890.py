'''
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
'''

# Tags: String

class Solution:
    def match(self, x, y):
        if len(x) != len(y): return False
        X, Y = list(x), list(y)
        if len(set(zip(X, Y))) == len(set(Y)) and len(set(Y)) == len(set(X)):
            return True
        else:
            return False

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ret = []
        for x in words:
            if self.match(x, pattern):
                ret.append(x)
        return ret