def guess(num: int) -> int:
    if num>pick:
        return -1
    elif num<pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            a=guess(mid)
            if a==-1:
                high=mid-1
            elif a==1:
                low=mid+1
            else:
                return mid
        