class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count =0
        for  i in arr1:
            good=True 
            for j in arr2:
                if abs(i-j) <=d:
                    good=False 
            if good == True:
                count +=1
        return count                