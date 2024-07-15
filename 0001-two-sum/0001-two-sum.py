class Solution(object):
    def twoSum(self, arr, target):
        dic = {}
        for key, value in enumerate(arr):
            second = target - value
            if second in dic:
                return [dic[second], key]
            dic[value] = key
        return 
        
#         arr.sort()
#         left = 0
#         counter  = 0
#         right = len(arr) - 1
        
#         while left < right:
#             cur_sum = arr[left] + arr[right]
#             if cur_sum == target:
#                 return [left, right]
#             elif cur_sum < target:
#                 left += 1
#             else:
#                 right -= 1
#         return None
            
