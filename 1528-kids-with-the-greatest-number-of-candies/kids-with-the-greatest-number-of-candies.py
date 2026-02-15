class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[False]* len(candies)
        maxx=max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxx:
                ans[i]=True 
            else:
                ans[i]= False
        return ans             