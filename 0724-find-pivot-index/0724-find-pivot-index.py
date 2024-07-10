class Solution(object):
    def pivotIndex(self, nums):
        psum = [0]
        for i in range(len(nums)):
            psum.append(psum[i] + nums[i])
        for i in range(len(psum) - 1):
            if psum[i] == psum[len(nums)] - psum[i + 1]:
                return i
        return -1