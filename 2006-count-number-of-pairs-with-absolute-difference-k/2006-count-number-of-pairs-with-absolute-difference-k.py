class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_dict = {}
        count = 0

        # Populate the dictionary with the frequency of each number in nums
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        # Iterate through the nums array and count the pairs
        for num in nums:
            # Check if there is a number that is `k` units greater than the current number
            if num + k in nums_dict:
                count += nums_dict[num + k]
            # Check if there is a number that is `k` units smaller than the current number
            if num - k in nums_dict:
                count += nums_dict[num - k]

            # To avoid double counting, decrease the count of the current number
            nums_dict[num] -= 1
            if nums_dict[num] == 0:
                del nums_dict[num]

        return count
                
        