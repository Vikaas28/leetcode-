class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq=Counter(s)
        #print(freq)
        st=[]
        seen=set()
        #print(freq)
        for  i in s:
            freq[i]-=1
            print(freq)
            if i in seen:
                continue
            while st and st[-1]>i and freq[st[-1]]>0:
                top=st.pop()
                seen.remove(top)    

            st.append(i)
            #print(i)    
            seen.add(i) 
        return "".join(st)       