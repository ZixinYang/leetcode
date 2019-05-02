'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
'''

# Tags: Two Pointers

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sort = [0]*len(A)
        i, j = 0, 0
        while j<len(A) and A[j]<0:
            j+=1
        i = j-1
        k = 0
        while i>=0 and j<len(A):
            if A[i]**2 <= A[j]**2:
                sort[k] = A[i]**2
                i-=1
                k+=1
            else:
                sort[k] = A[j]**2
                j+=1
                k+=1
        while i>=0:
            sort[k] = A[i]**2
            i-=1
            k+=1
        while j<len(A):
            sort[k] = A[j]**2
            j+=1
            k+=1
        return sort