class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        left = 0
        right = len(nums) - 1
        
        counter  = 0
        while left < right:
            curr = nums[left] + nums[right]
            if curr < k:
                left += 1
            elif curr > k:
                right -= 1
            else:
                counter += 1
                left += 1
                right -= 1
        return counter
            
            
        