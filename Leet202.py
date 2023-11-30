class Solution:
    def isHappy(self, n: int) -> bool:
        c=0
        add=0
        if n==1 or n==7:
            return True
        elif n<10:
            return False
        while c!=1:
            for i in str(n):
                new=pow(int(i),2)
                add=add+new
            n=add
            c=add
            if add==7:
                return True
            elif add<10 and add>1:
                return False
            add=0
        return True



        