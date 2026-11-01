class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        def count_set(n):
            count=0
            while n > 0:
                #n&=n-1 # count n=n&(n-1)
                count+=n&1
                n>>=1
            return count 
        s1=count_set(a)
        s2=count_set(b)
        if s1>=s2:
            return s1*s2 
        else:
            return s2//s1           
        