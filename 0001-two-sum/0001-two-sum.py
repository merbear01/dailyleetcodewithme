class Solution(object):
    def twoSum(self, arr, target):
        dic = {}
        for key, value in enumerate(arr):
            second = target - value
            if second in dic:
                return [dic[second], key]
            dic[value] = key
        return 


