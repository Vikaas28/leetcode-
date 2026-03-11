class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Frequency map
        freq = {}
        arr=[]
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        return sorted(freq, key=freq.get,reverse=True)[:k]