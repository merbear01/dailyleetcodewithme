class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Initialize an array 'answer' with the same length as 'nums'
        answer = [1] * len(nums)

        # Calculate the product of all the numbers to the left of the current index
        left_product = 1
        for i in range(len(nums)):
            answer[i] *= left_product
            left_product *= nums[i]

        # Calculate the product of all the numbers to the right of the current index
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer

        
        