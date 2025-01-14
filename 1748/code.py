
from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([item for item in nums if nums.count(item) == 1])


print(Solution().sumOfUnique([1,2,3,2]))
print(Solution().sumOfUnique([1,1,1,1]))
