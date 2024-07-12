class Solution(object):
    def kthFactor(self,n, k):
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:  # Avoid duplicate factors
                    factors.append(n // i)
        factors.sort()
        if k <= len(factors):
            return factors[k - 1]
        return -1  # Return -1 if k is out of bounds
