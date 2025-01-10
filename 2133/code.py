from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        example = set(range(1, len(matrix[0])+1))

        return all(example == set(x) for x in matrix + list(zip(*matrix)))


print(Solution().checkValid([[1,2,3],[3,1,2],[2,3,1]]))
