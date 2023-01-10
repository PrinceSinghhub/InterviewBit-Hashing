from collections import Counter


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        mydic = Counter(A)

        count = 0
        for i in mydic.values():
            if i % 2 != 0:
                count += 1
            if count > 1:
                return 0

        return 1

