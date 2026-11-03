class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        count =0
        for i in range(len(hours)):
            
            for j in range(i+1,len(hours)):
                summ=hours[i]+hours[j]
                
                if summ %24==0 :
                    count +=1
       #     summ=hours[i]+hours[i+1]
        #     if summ % 24==0:
        #         count+=1
        return count          
        