class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lst = []
        for l in grid:
            lst.extend(l)
        # return lst
        pot = 0
        for items in lst:
            if items < 0:
                pot += 1
        return pot