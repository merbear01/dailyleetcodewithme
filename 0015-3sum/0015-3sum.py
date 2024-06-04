class Solution(object):
    def threeSum(self, s):
        ans = []
        s.sort()

        for i in range(0, len(s)):
            if i > 0 and s[i] == s[i-1]:
                continue
            j = i + 1
            k = len(s) - 1
            while j < k:
                sum = s[i] + s[j] + s[k]

                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    temp = [s[i], s[j], s[k]]
                    ans.append(temp)
                    j+= 1
                    k -= 1 
                    while j < k and s[j] == s[j - 1]:
                        j += 1
                    while j < k and s[k] == s[k + 1]:
                        k -= 1

        return ans