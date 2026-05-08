class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in has:
                return [has[com],i]
            has[nums[i]]=i
        return has       