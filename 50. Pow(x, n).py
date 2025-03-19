class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = abs(n)

        if n % 2 == 0:
            half = self.myPow(x, n//2)
            return half * half
        else:
            half = self.myPow(x, (n-1)//2)
            return x * half * half


            