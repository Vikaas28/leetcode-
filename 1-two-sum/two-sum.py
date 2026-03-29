class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      has={}
      for i in range(len(nums)):
        comm=target -nums[i]
        if  comm in has:
            return [ has[comm],i]
        has[nums[i]]=i
      return []        