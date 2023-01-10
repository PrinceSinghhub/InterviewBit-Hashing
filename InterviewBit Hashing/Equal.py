class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):

        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(1, n):
                    for l in range(k + 1, n):
                        if not (i == j or i == k or k == l or j == k or j == l or i == l) and A[i] + A[j] == A[l] + A[k]:
                            return [i, j, k, l]
        return []
