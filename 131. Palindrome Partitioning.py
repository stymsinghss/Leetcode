from typing import List

class Solution:
    def checkPalindrome(self, string: str) -> bool:
        return string == string[::-1]

    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        self.getPalindromes(s, palindromes, 0, [])
        return palindromes

    def getPalindromes(self, string: str, palindromes: List[str], idx: int, temp: List[str]) -> None:
        if idx == len(string):
            palindromes.append(temp[:])
            return

        for i in range(idx, len(string)):
            window = string[idx:i+1]
            if self.checkPalindrome(window):
                temp.append(window)
                self.getPalindromes(string, palindromes, i+1, temp)
                temp.pop()

