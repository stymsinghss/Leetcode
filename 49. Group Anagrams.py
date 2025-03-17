from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        anagram_mapper = dict()
        for word in strs:
            sorted_word_list = sorted(word)
            sorted_word = ''.join(sorted_word_list)
            if sorted_word in anagram_mapper:
                anagram_mapper[sorted_word].append(word)
            else:
                anagram_mapper[sorted_word] = [word]
        return list(anagram_mapper.values())