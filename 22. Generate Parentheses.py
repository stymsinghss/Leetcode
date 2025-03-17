from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paran = []

        self.gen(n, 0, 0, paran, "")
        return paran

    def gen(self, n: int, oc: int, cc: int, paran: List[str], dummy: str) -> None:
        if len(dummy) == n * 2:
            paran.append(dummy)
            return

        if oc < n:
            self.gen(n, oc+1, cc, paran, dummy + "(")

        if cc < oc:
            self.gen(n, oc, cc+1, paran, dummy + ")")
