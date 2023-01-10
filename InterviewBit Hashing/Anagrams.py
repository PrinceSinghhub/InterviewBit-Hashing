from collections import OrderedDict


class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        m = OrderedDict()
        for idx, s in enumerate(A):
            ss = ''.join(sorted(s))
            if ss in m:
                m[ss].append(idx + 1)
            else:
                m[ss] = [idx + 1]
        return list(m.values())

