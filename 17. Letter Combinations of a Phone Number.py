from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_word_mapper = {
            "2": ["a","b","c"],
            "3": ["d" ,"e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        combs = []
        self.generate(digits, digit_word_mapper, combs, [], 0)
        return combs

    def generate(self, digits, digit_word_mapper, combs, temp, idx) -> None:
        if len(temp) == len(digits):
            combs.append(''.join(temp[:]))
            return

        chars = digit_word_mapper[digits[idx]]
        # print("chars - ", chars)

        for char in chars:
            temp.append(char)
            self.generate(digits, digit_word_mapper, combs, temp, idx+1)
            temp.pop()