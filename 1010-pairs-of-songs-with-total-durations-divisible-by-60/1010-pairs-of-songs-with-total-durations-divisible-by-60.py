class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        freq = {}
        count  = 0
        for items in time:
            remains = items % 60
            complement = (60 - remains) % 60
        
            if complement in freq:
                count += freq[complement]

            if remains in freq:
                freq[remains] += 1
            else:
                freq[remains] = 1
    
        return count

        # this is the brute force apporach and would take 0(n^2) meaning it may not work for larger arrays
#         count = 0
#         for i in range(len(time)):
#             for j in range(i+1, len(time)):
#                 if (time[i] + time[j]) % 60 == 0:
#                     count += 1
                    
#         return count