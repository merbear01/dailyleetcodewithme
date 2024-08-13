class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        for items in arr:
            if items in dic:
                dic[items] += 1
            else:
                dic[items] = 1
        
        freq = set()
        for values in dic.values():
            if values in freq:
                return False
            freq.add(values)
        return True