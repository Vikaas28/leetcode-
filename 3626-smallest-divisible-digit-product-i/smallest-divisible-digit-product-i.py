class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            curr=1
            temp=n
            while temp>0:
                curr*=temp%10
                temp//=10
                
            if curr %t ==0:
                return n 
            n+=1        



        