class Solution(object):
    def isPalindrome(self, x):
        sum=0
        if x<0:
            return False
        else:
            temp=x
            while(x>0):
                r=x%10
                sum=(sum*10)+r
                x=x//10
                x=int(x)
            if temp==sum:
                return True
            else:
                # a="false"
                return False
        """
        :type x: int
        :rtype: bool
        """
        