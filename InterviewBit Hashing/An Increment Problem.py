class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        for i in range(0, len(A)):
            j = A.index(A[i])
            if i != j:
                A[j] += 1

        return A
