class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        
        st=set()
        avg=0

        while(l<r):
            avg=(nums[l]+nums[r])/2
            st.add(avg)
            l+=1
            r-=1
        return len(st)    
