class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        #lst=[]
        l=0 
        #h=len(nums)-1


        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            h=len(nums)-1
            while l<h:
                total=nums[i]+nums[l]+nums[h]
                if total==0:
                    triplets.append([nums[i],nums[l],nums[h]])
                    while l<h and nums[l]==nums[l+1]:
                        l+=1
                    while l<h and nums[h]==nums[h-1]:
                        h-=1
                    l+=1
                    h-=1
                elif total<0:
                    l+=1
                else :
                    h-=1                    


            
        
        return triplets            
