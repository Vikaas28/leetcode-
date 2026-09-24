class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i , v in enumerate(nums):
            temp=v 
            summ=0
            
            while temp >0 :
                summ+=temp%10
                
                #print(temp)
                temp//=10
                #print(temp, summ)
            if summ==i:
                return i 
        return -1            

        