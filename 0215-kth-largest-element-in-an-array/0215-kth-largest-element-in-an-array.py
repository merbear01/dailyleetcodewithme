class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        return heapq.nlargest(k, nums)[-1]
    
    def sliding_window_adjusted(nums, k):
        kth_largest = find_kth_largest(nums, k)
        window_size = kth_largest
        result = []

        for i in range(len(nums) - window_size + 1):
            window = nums[i:i + window_size]
            result.append(max(window))  # Example operation: finding the maximum in the window

        return result