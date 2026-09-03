class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # nums2=[]
        # for i in range(len(nums1)):
        #     if i %2 ==0 :
        #         nums2.append(nums1[i])
        #     for j in range(len(nums1)):
        #         if nums1[i]-nums1[j]>=1 and j != i :
        #             nums2[i]=nums1[i] - nums1[j] 
        #             return True 
        #         else:
        #             nums2[i]=nums1[i]
        #             return True 
        # return False  
        #odd=any(x % 2!=0 for x in nums1)
        # if not odd :
        #     return True\
        odd=[ x for x in nums1 if x%2!=0]
        if not odd :
            return True
        mini=min(odd)
        #mini=min( x for x in nums1 if x %2 !=0 ) 
        for i in nums1:
            if i %2 ==0 and  i < mini:
                return False
        return True            
              
