# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        start = 1
        end  = n
        while start <= end:
            pick = start + (end-start)// 2
            if guess(pick) == 0:
                return pick
            elif guess(pick) == 1:
                start = pick + 1
            else:
                end = pick - 1
        return -1
        