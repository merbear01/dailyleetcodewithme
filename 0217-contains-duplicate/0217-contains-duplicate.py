class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        traverse = {}
        for items in nums:
            if items in traverse:
                return True
            traverse[items] = 1
                
        return False
        