class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a=format(n,"b")
        c=0
        for i in range(len(a)-1):
            if a[i]==a[i+1]:
                return False
            else:
                c=c+1
        return c==len(a)-1
            

        