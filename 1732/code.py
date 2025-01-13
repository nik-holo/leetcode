
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sums = []
        for i in range(len(gain)):
            sums.append(sum(gain[:i+1]))
        max_sum = max(sums)
        return  0 if max_sum < 0 else max_sum

print(Solution().largestAltitude([-5,1,5,0,-7]))
print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))
print(Solution().largestAltitude([44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]))
