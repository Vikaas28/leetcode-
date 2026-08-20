class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n=len(nums)
        arr=[0]*n
        poss=0
        neg=1
        for i in nums:
            if i>0 :
                arr[poss]=i
                poss+=2
            else:
                arr[neg]=i
                neg+=2
        return arr             
        
        