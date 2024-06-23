class Solution(object):
    def isSubsequence(self, s, t):
        new_s= 0 
        new_t= 0
        while new_s < len(s) and new_t < len(t):
            if s[new_s] == t[new_t]:
                new_s += 1
            new_t += 1
        return new_s == len(s)