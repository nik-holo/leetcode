
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
            index_map = {word: i for i, word in enumerate(list1)}
            min_sum = float('inf')
            result = []

            for i, word in enumerate(list2):
                if word in index_map:
                    index_sum = i + index_map[word]
                    if index_sum < min_sum:
                        min_sum = index_sum
                        result = [word]
                    elif index_sum == min_sum:
                        result.append(word)

            return result

print(Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))
