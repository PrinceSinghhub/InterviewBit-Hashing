class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return self.atMostBodd(A,B) - self.atMostBodd(A,B-1)
    def atMostBodd(self,A,B):
        l = 0
        r = 0
        count = 0
        res = 0
        while r < len(A):
            if A[r] % 2 == 1:
                count += 1
            while l < r and count > B:
                if A[l] % 2 == 1:
                    count -= 1
                l += 1
            if count <= B:
                res += r - l + 1
            r += 1
        return res