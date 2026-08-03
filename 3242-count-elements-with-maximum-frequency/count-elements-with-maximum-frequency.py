class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=Counter(nums)
        maxFreq=max(freq.values())
        print(maxFreq)
        count=0
        for key , val in freq.items():
            if val == maxFreq:
                count +=1
             
       
        return count *maxFreq            