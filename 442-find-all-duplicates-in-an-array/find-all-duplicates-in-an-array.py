class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        arr=[]
        for i in nums:
            freq[i]= freq.get(i , 0) + 1 
        for k, v in freq.items():
            if  v > 1:
                arr.append(k)
        return arr             
            