
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # better solution
        # return Counter(target) == Counter(arr)
        arr_set = set(arr)
        target_set = set(target)
        return sorted(arr) == sorted(target) or target_set in arr_set

print(Solution().canBeEqual([1,2,3,4], [2,4,1,3]))
print(Solution().canBeEqual([7], [7]))
print(Solution().canBeEqual([3,7,9], [3,7,11]))
print(Solution().canBeEqual([1,2,2,3], [1,1,2,3]))
