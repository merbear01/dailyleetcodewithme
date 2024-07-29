class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_digit = -1
        second_max_digit = -1

        for char in s:
            if char.isdigit():
                digit = int(char)
                if digit > max_digit:
                    second_max_digit = max_digit
                    max_digit = digit
                elif digit < max_digit and digit > second_max_digit:
                    second_max_digit = digit

        return second_max_digit
