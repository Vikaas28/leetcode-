class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l=0
        h=len(height)-1
        res=0

        while(l<=h):
            width=h-l
            area=width*min(height[l],height[h])
            res=max(res,area)
            if height[l]<height[h]:
                l+=1
            elif height[l]>height[h]:
                h-=1
            else:
                h-=1
        return res                 
