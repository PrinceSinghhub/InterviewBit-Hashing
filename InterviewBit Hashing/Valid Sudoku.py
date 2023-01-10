class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        for i in range(9):
            if not self.isValidArray(list(A[i])) \
                    or not self.isValidArray([A[j][i] for j in range(9)]) \
                    or not self.isValidArray([A[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] for j in range(9)]):
                return 0
        return 1

    def isValidArray(self, arr):
        s = set()
        for x in arr:
            if x in s:
                return False
            if x != '.':
                s.add(x)
        return True


