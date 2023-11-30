class Solution:
    def addDigits(self, num: int) -> int:
        n=len(str(num))
        a=0
        if n==1:
            return num
        while num>9:
            a=0
            for i in str(num):
                a=a+int(i)
            num=a
        return a
        