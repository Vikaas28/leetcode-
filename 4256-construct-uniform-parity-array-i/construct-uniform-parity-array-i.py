class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        flag=False
        nums2=[]
        for i  in range(len(nums1)):
            for j in range(len(nums2)):
                if j !=i :
                    nums2[i]=nums1[i]-nums1[j]
        count =0            
        for i in range(len(nums2)):
            if nums2[i]%2!=0:
                count +=1 
        if count == len(nums2):
            return True 
        return False                        
        