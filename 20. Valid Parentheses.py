class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        stack = []
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in ['[','{','(']:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    top_element = stack[-1]
                    if map[char] != top_element:
                        return False
                    stack.pop()
        return len(stack) == 0 