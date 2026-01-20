class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        seen=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key ,value in freq.items():
            if value ==1:
                seen.append(key)
        return seen          