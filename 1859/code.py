class Solution:
    def sortSentence(self, s: str) -> str:
        word = sorted(s.split(), key=lambda x: x[-1])
        return " ".join([w[:-1] for w in word])

print(Solution().sortSentence("is2 sentence4 This1 a3"))
