class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hay = list(haystack)
        need = list(needle)
        i, j = 0, 0
        new_stack = []
        while i < len(hay) and j < len(need):
            if hay[i] == need[j]:
                new_stack.append(hay[i])
                i += 1
                j += 1
                if j == len(need):  # When the needle is fully matched
                    return i - j    # Return the starting index of the match
            else:
                if new_stack:
                    i = i - len(new_stack) + 1  # Reset i to the next character after the first matched character
                else:
                    i += 1
                new_stack = []
                j = 0  # Reset j to start matching from the beginning of the needle again

        return -1  # If no match is found
