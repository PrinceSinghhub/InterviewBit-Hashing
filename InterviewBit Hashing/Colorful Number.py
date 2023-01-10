from functools import reduce
class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        products = set()
        str_num = str(A)
        for i in range(len(str_num)):
            for j in range(i + 1, len(str_num) + 1):
                product = reduce(lambda x, y: x * y, map(int, list(str_num[i:j])))
                if product in products:
                    return 0
                products.add(product)
        return 1
