class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        st=[]
        for  i in range(len(s)):
            if s[i]=="(":
                st.append(score)
                score=0
            else:
                ins =max(2 * score,1)
                score=st.pop()+ins
        return score        
            #st.append(s[i])
        #return score                     

            



