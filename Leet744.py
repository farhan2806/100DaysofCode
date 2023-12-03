class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left=0
        right=len(letters)-1
        if target>letters[right] or target<letters[0]:
            return letters[0]
        while left<=right: 
            mid= (left+right)//2
            if letters[mid]<=target:
                left=mid+1
            else:
                right=mid-1
        if left<len(letters):
            return letters[left]
        return letters[0]


        