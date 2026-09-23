class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        l=0
        mn=-1
        summ=0
        target=sum(nums)-x
        
        mp={}
        for i in range(len(nums)):
            summ+=nums[i]
            #mp[summ]=mp.get(i,0)
            
            while summ>target  and l<=i  :
                summ-=nums[l]
                l+=1
            if summ==target:
                mn=max(mn,i-l+1)
        return len(nums)- mn if mn !=-1 else -1               