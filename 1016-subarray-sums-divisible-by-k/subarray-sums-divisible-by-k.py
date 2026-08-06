class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp={0:1}
        count=0
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix % k in mp:
                count+=mp.get(prefix%k,0)
            mp[prefix%k]=mp.get(prefix%k,0)+1
        return count         