class Solution:
    def decode(self, encoded: list[int]) -> list[int]:
        n=len(encoded)+1
        xor=0
        for i in range(1, n+1):
            xor ^=i 
        odd=0
        for i in range(1, len(encoded),2) :
            odd ^= encoded[i]
        perm=[xor ^ odd]    
        for i in range(len(encoded)):
            perm.append(perm[-1]^encoded[i]) 
        return perm     
