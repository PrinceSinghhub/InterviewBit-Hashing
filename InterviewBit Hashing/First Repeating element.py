class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # mp = set()
        if len(A) == len(set(A)):
            return -1
        for i in A:
            if A.count(i) > 1:
                return i

        return -1

