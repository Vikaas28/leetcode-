class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix=0
        freq={0:-1}
        l=0
        if len(nums)==1:
            return False
        for i in range(len(nums)):
            #sum mod k
            prefix=(prefix+nums[i])%k
            if prefix in freq:
                if (i - freq[prefix])>1:
                    return True
            if prefix  not in freq:
                freq[prefix]=i
        return False            