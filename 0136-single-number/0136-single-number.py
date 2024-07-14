class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for items in nums:
            if items not in counter:
                counter[items] = 1
            else:
                counter[items] += 1
                
        for item, freq in counter.items():
            if freq == 1:
                return item