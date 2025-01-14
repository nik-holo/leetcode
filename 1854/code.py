
from collections import defaultdict
from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years_count = defaultdict(int)
        for person in logs:
            for year in range(person[0], person[1]):
                years_count[year] += 1

        max_count = max(years_count.values())

        lowest_year_with_max_count = min(year for year, count in years_count.items() if count == max_count)

        return lowest_year_with_max_count

# print(Solution().maximumPopulation([[1993,1999],[1998,2010],[1992,2011]]))
print(Solution().maximumPopulation([[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]))
