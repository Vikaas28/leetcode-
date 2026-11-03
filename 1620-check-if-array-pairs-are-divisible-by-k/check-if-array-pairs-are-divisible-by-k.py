class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        map={}
        # a % k = r1 
        # b % k = r2 
        # then r1+r2=k 
        map={}
        #for i in range(0,len(arr),2):
        for i in range(len(arr)):   
            rem= (arr[i] % k + k) % k  
            map[rem]=map.get(rem,0)+1
        for rem in map:
            if rem==0:
                if map[rem] % 2 !=0:
                    return False 
            else:


                poss=k-rem

                if map.get(poss,0)!=map[rem]:
                    return False


            
        return True         

        # for i  in range(len(arr)-1):
        #     if (arr[i]+arr[i+1]) % k==0 :
        #         return True 
        # return False         