class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy = ""
        if len(s) < 3:
            return s

        last = ""
        prelast = ""

        for char in s:
            if char != last or char != prelast:
               fancy = fancy + char
               prelast = last
               last = char

        return fancy


print(Solution().makeFancyString("aaabaaaa"))
