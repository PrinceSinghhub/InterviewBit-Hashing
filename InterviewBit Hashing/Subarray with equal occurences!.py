from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A); ans = 0; diff=0
        d = defaultdict(int)
        d[0] = 1

        for x in A:
            if x==B: diff+=1
            if x==C: diff-=1
            ans+= d[diff]
            d[diff]+= 1

        return ans

