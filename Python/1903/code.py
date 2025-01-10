class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):  # Iterate from the end to the start
            if num[i] in "13579":
                lon = num[0:i+1]
                break

        return lon

print(Solution().largestOddNumber("35427"))
