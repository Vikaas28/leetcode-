class Solution:
    def sumAndMultiply(self, n: int) -> int:
        summ=0
        digit=0
        n=str(n)
        
        
        for i in n :
            s=int(i)
            if s ==0 :continue
            summ+=s
            #print(summ)
            #print(s)
            digit=digit*10 +s
        return digit * summ
         
        

            

        #return summ  