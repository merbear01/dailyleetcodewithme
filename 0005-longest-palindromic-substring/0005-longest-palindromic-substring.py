class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0
    
        for i in range(len(s)):
            # check odd length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left +1) > resLen:
                    res = s[left : right + 1]
                    resLen = right - left + 1

                left -= 1
                right += 1

           
            # check even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left : right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

        return res