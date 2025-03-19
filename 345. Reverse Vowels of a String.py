class Solution:
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        left, right = 0, len(s)-1
        vowels = set("aAeEiIoOuU")
        while left <= right:
            if slist[left] in vowels and slist[right] in vowels:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1
            elif slist[left] in vowels and not slist[right] in vowels:
                right -= 1
            else:
                left += 1
        return ''.join(slist)