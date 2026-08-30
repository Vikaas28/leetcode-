class Solution:
    def minDeletions(self, s: str) -> int:
        freq=Counter(s)
        #print(freq)
        seen=set()
        count=0
        for key ,  value in freq.items():
            while value > 0 and value in seen:
                value -=1 
                count +=1
            if value > 0 :    
                seen.add(value)
        return count         
        #print(len(freq))
        #return math.ceil(len(freq)/2)
            


        