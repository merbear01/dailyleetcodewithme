class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        num_str  = ''.join(str(digit) for digit in num)
        add = int(num_str) + int(k)
        string = [int(x) for x in str(add)]
        return string