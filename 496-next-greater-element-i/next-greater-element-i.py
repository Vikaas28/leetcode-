class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        ans=[]
        nextt={}
        for  i in range(len(nums2)-1,-1,-1):
            num=nums2[i]
            #st.append(num)
            while st and st[-1]<=num:
                st.pop()
            if st :
                nextt[num]=st[-1]
            else:
                nextt[num]=-1
            st.append(num)    
                
        for i in nums1:
            ans.append(nextt[i])
        return ans                    