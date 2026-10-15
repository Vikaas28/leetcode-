class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count =0 
        c=[]
        mp={}
        for i in range(len(A)):
            mp[A[i]]=mp.get(A[i] , 0)+1
            if mp[A[i]]==2:
                count +=1
            mp[B[i]]=mp.get(B[i],0)+1
            if mp[B[i]]==2:
                count +=1
            c.append(count)
        return c             
        