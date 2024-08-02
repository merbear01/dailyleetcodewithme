class Solution(object):
    def runningSum(self, nums):
        curr = 0
        arr = []
        for items in nums:
            curr += items
            arr.append(curr)
            if len(nums) <= 1:
                return arr
        return arr