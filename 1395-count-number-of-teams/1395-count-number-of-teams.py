class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        counter = 0
        
        greater = [0] * n
        less = [0] * n

        for i in range(n):
            for j in range(i):
                if rating[i] > rating[j]:
                    greater[i] += 1
                    counter += greater[j]
                elif rating[i] < rating[j]:
                    less[i] += 1
                    counter += less[j]

        return counter
        