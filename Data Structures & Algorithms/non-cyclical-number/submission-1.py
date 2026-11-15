class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)

            n = self.squareOfSum(n)
            if n == 1:
                return True

        return False
    

    def squareOfSum(self, n):
        output = 0

        while n:
            digit = n % 10
            digit = digit  ** 2
            output = output + digit
            n = n // 10
        return output