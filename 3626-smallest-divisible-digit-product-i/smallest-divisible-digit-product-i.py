class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            curr=1
            for i in str(n):
                curr*=int(i)
            if curr % t ==0:
                return n 
            n+=1        