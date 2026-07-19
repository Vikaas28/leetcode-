class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        freq=Counter(s)
        seen=set()
        st=[]
        for  i in s:
            freq[i]-=1
            if i in seen:
                continue
            while st and st[-1]> i and freq[st[-1]]>0:
                #print(freq[st[-1]])
                top=st.pop()
                seen.remove(top)


            st.append(i)
            seen.add(i)    
        return "".join(st)
