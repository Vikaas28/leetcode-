class Solution:
  def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        index=abs(nums[i])-1
        #print(index)
        if nums[index]>0:


            nums[index]=-nums[index]
    #print(nums)
    res=[]    
    for i in range(len(nums)):
        if nums[i]>0:
            res.append(i+1)
    return res            