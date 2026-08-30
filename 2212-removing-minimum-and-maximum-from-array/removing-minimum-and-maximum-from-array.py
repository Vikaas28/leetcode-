class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # count=0
        # mini=nums[0]
        # maxx=nums[0]
        # while maxx>max(nums) and mini> min(nums):
        #     # if maxx ==max(nums) and mini==min(nums):
        #         del maxx 
        #         del mini
        #         count+=1
        # return count 
        maxx=nums[0]
        mini=nums[0] 
        maxx_ind=0
        min_ind=0
        for i , v in enumerate(nums):
            if v < mini:
                mini=v
                min_ind=i
            if v> maxx:
                maxx=v
                maxx_ind=i

           
        left =min(maxx_ind,min_ind)
        right =max(maxx_ind,min_ind) 
        #front 
        front=right+1
        #back
        n=len(nums)
        back=n-left
        #both 
        both =(left +1) + (n-right)
        return min(front, back ,both)       

                 

        