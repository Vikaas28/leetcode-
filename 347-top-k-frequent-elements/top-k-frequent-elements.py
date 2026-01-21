class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Frequency map
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Step 2: Bucket list
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Collect top k frequent
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
