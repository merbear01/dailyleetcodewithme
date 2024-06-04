class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        # Check all possible substring lengths from 1 to n//2
        for i in range(1, n // 2 + 1):
            if n % i == 0:  # Check if i is a divisor of n
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
        return False