class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        A, B, C = set(A), set(B), set(C)
        ans = A.intersection(B).union(B.intersection(C)).union(C.intersection(A))
        return sorted(ans)

