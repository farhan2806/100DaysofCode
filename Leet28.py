class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        h=len(haystack)
        for i in range(h):
            if haystack[i:i+n]==needle:
                return i
        return -1
        