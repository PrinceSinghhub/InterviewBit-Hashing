class Solution:
    def lszero(self, A):
        d={0:-1}
        s=0
        l=-1
        a,b=-1,-1
        for i in range(len(A)):
            s=s+A[i]
            if s in d:
                if l<(i-d[s]):
                    a=d[s]+1
                    b=i
                    l=i-d[s]
            else:
                d[s]=i
        return A[a:b+1]
