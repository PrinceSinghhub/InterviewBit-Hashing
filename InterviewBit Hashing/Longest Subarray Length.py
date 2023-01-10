class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = 0

        curr = 0
        first, last = {}, {}
        first[0] = -1
        last[0] = -1

        for i in range(len(A)):
            curr += 1 if A[i] == 1 else -1
            if curr not in first:
                first[curr] = i
            last[curr] = i

        for key in last:
            if key - 1 in first:
                ans = max(ans, last[key] - first[key - 1])

        return ans




