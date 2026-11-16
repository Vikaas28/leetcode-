class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        #count=0
        t=0
        for i in range(len(arr)):
            summ=0
            for j in range(i,len(arr)):
                #summ+=nums[j]
                summ+=arr[j]
                lenn=j-i+1
                if lenn %2!=0:
                    t+=summ                   #count=summ
        return t      
        