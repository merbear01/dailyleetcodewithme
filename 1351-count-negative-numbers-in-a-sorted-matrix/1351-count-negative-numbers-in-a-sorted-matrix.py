class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        negative_pot = 0
        for rows in grid:
            for items in rows:
                if items < 0:
                    negative_pot += 1
        return negative_pot
        # new_lst = []
        # for l in grid:
        #     new_lst.extend(l)
        # # return lst
        # negative_pot = 0
        # for items in new_lst:
        #     if items < 0:
        #         negative_pot += 1
        # return negative_pot