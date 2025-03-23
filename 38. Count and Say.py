class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        input = "11"
        for i in range(3, n+1):
            count = 1
            input += "$"
            output = ""

            for j in range(1, len(input)):
                if input[j] == input[j-1]:
                    count += 1
                else:
                    output+=str(count)
                    output+=input[j-1]
                    count = 1
            input = ''.join(output)
        return input
