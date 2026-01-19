class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        h=len(height)-1
        res=0
        while(l<h):
            area=(h-l)*min(height[l],height[h])
            res=max(res,area)
            if height[l]>height[h]:
                h-=1   # eleminate the right 
            elif height[l]<height[h]:
                l+=1
            else:
                h-=1
        return res #  max area                    
        