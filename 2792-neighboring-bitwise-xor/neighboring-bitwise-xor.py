class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # xor=0
        # for  i in derived:
        #     xor = xor ^ i
        # return xor ==0 

        n=len(derived)
        og=[0]*(n+1)
        og[0]=0

        if n==1 and derived[0]==1:
            return False 
        for i in range(n-1):
            og[i+1]=og[i]^derived[i]
        if og[n-1]^og[0]==derived[n-1]:
            return True  
        else:
            derived[n-1]=og[n-1]^og[n]
        og[0]=1
        if og[n-1]^og[0]==derived[n-1]:
            return True 
        else:
            derived[n-1]=og[n-1]^og[n]  

        return False                   