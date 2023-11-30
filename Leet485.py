class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        a=0
        n=0
        for i in range(len(nums)):
            if nums[i]==1:
                a=a+1
            if nums[i]==0:
                a=0
            if a>n:
                n=a
        return n

        