'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:

Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''

#

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        for i in range(len(S)):
            if S[i].isalpha():
                low = S[i].lower()
                up = S[i].upper()
                if i==0:
                    ans.append(low)
                    ans.append(up)
                else:
                    ans = ans*2
                    for j in range(len(ans)):
                        if j<len(ans)//2:
                            ans[j]+=low
                        else:
                            ans[j]+=up
            else:
                if i==0:
                    ans.append(S[i])
                else:
                    for j in range(len(ans)):
                        ans[j]+=S[i]
        return ans