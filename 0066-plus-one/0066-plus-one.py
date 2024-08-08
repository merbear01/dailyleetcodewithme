class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        s = [str(integer) for integer in digits]
        a_string = "".join(s)
        res = int(a_string)
        add = res + 1
        new_dig = [int(ch) for index, ch in enumerate(str(add))]
        return new_dig