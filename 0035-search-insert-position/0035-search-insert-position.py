class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right)// 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right =  middle - 1
            else:
                return middle
        return left # this ensures that in the case of a missing value, we insert in an ordered format
                