class Solution(object):
    def romanToInt(self, s):
        final=0
        prev=0
        values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in s:
            val=values[i]
            if val>prev:
                final=final+val-2*prev
            else:
                final = final+val
            prev=val
        return final
        """
        :type s: str
        :rtype: int
        """
        