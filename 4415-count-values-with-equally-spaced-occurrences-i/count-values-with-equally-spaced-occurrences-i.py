class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count =0
        ind=defaultdict(list)
        freq=Counter(nums)
        for i , v in enumerate(nums):
            # if v.count()==3  :
            #     count+=1
            ind[v].append(i)
        print(ind)  
        for key , val in ind.items():
            if len(val)==3:
                i1,i2,i3=val
                if i2-i1==i3-i2:
                    count+=1
        return count                   
                
        # for key , val in freq.items():
        #     if count ==val:

            
        