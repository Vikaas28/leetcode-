class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()


        def perm(path):
            if path==len(nums):
                res.append(nums[:])
                return 
            used =set()    
            for i in range(path,len(nums)):
                if i>path and nums[i]==nums[path]:
                    continue
                if nums[i] in used:
                    continue
                used.add(nums[i])        
                
                nums[path],nums[i]=nums[i],nums[path]
                perm(path+1)
                nums[path],nums[i]=nums[i],nums[path]
        perm(0)
        return res             

        