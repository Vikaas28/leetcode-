class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key ,value in freq.items():
            if value >=2 :
                return key     