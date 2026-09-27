class Solution:
    def countCollisions(self, directions: str) -> int:

        ans=[]
        # count=0
        # i=0
        # j=len(directions)-1
        # while i<len(directions) and directions[i]=="L":
        #     i+=1
        # while j > 0 and directions[j]=="R":
        #     j-=1
        # while i <=j:
        #     if directions[i] !="S":
        #          count+=1
        #     i+=1


        # return count 
        ans=[]
        count=0
        j=len(directions)-1
        for i in directions:
            if i =="L":
                if ans and ans[-1]=="R":
                    count+=2
                    ans.pop()
                    i="S"
                elif ans and ans[-1]=="S":
                    count+=1
                    i="S"
            if i =="S":
                while ans and ans[-1]=="R":
                    count+=1
                    ans.pop()
                #elif ans and ans[-1]=="S":
                    #count+=1
                    #i=="S"

            
            ans.append(i)  
        return count         

        