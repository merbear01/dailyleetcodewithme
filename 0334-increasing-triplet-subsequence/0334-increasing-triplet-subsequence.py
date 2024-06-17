class Solution(object):
    def increasingTriplet(self, nums):
        one = float("inf")
        two = float("inf")
        for n in nums:
            if n > two:
                return True
            if n <= one:
                one = n
            elif n <= two:
                two = n