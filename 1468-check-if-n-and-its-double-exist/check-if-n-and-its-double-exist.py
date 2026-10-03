class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen=set()
        for i in range(len(arr)):
            
            if arr[i]<<1 in seen or (arr[i]%2 ==0  and (arr[i]>>1) in seen):

                return True
            seen.add(arr[i])

        return False        
        