class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq=Counter(nums)
        streak=0
        #print(freq.keys())
        for i in freq:
            
            if i-1 not  in freq:
                curr=i
                maxln=1
                while curr+1  in freq:
                    curr+=1
                    

                    maxln+=1
                    print(curr,maxln)
                streak=max(streak,maxln)    

        return streak  
            

           
        return maxln            