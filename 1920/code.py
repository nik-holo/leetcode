
from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result

print(Solution().buildArray([0,2,1,5,3,4]))
