class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        summ =0
        prod=1

        while temp > 0:
            temps = temp %10
            summ+=temps
            prod*=temps

            temp//=10
        t=summ + prod 
        return n%t==0
        #return False          
        