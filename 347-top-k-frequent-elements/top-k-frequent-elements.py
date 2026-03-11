class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Frequency map
        freq = {}
        arr=[]
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        buck =[[] for _ in range(len(nums)+1)]
        for num , i in freq.items():
            buck[i].append(num)
        res=[]    
        for  j in range(len(buck)-1,0,-1):
            for num in buck[j]:
                res.append(num)
                if len(res )==k:
                    return res    