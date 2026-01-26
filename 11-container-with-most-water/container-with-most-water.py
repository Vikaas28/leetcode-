class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        h=len(height)-1
        he=height
        res=0
        while l<=h:
            width=h-l

            area=width * min(he[l],he[h])
            res=max(res,area)
            if he[l]<he[h]:
                l+=1
            elif he[l]>he[h] :
                h-=1   
            else:
                h-=1
        return res                 