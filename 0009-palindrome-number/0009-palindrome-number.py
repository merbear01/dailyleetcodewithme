class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        x = list(x)
        for items in x:
            if x[0::] == x[::-1]:
                continue
            return False
        return True