class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        c=len(strs[0])
        result=""
        for i in range(c):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return result
            result=result+s[i]
        return result
        