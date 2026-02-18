class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=len(num)-1
        while n>=0 and k>0:
            k+=num[n]
            num[n] = k%10
            k//=10
            n-=1

        while k>0:
            num.insert(0,k%10)
            k//=10    
        return num    