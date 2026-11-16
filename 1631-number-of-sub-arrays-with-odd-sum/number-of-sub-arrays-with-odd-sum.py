class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod=10**9 + 7 
        odd=0
        even =1
        summ=0
        total=0
        for i in range(len(arr)):
            summ+=arr[i]
            if summ %2!=0:
                #odd+=1
                total=(total+even) %mod
                odd+=1
            else:
                total=(total+odd)%mod
                even +=1
        return total            