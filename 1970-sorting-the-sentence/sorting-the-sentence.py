class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = sorted((word[-1], word[:-1]) for word in s.split())
        return " ".join(pair[1] for pair in sentence)