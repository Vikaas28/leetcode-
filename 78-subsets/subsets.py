class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(i,p):
            res.append(p.copy())
            
            for j in range(i,len(nums)):
                p.append(nums[j])
                back(j+1,p) 
                p.pop()  
        back(0,[])
        return res      