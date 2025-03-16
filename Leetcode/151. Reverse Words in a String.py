class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        for word in s.strip().split():
            if word != "":
                words.append(word)
        return " ".join(words[::-1])
    