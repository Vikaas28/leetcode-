class Solution:
    def countBits(self, n: int) -> list[int]:
        def count(n):
            count=0
            while(n!=0):
                count+=1
                n=n&(n-1)
            return count
        return [ count(i) for i in range(n+1)]        
        