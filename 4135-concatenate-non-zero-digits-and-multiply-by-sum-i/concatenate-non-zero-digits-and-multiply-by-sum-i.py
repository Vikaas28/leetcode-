class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits=[i for i in str(n) if i !='0']
        if not digits:
            return 0
        x=int("".join(digits))
        summ=sum(int(d) for d in digits)
        return x*summ

        #return summ  