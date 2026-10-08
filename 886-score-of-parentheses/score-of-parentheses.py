class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        st=[]
        for  i in range(len(s)):
            if s[i]=="(":
                st.append(score)
                score=0
            else:
                ins=max(1, 2*score)
                score=st.pop()+ ins
                # if s[i-1]=="(":
                #     score=st.pop()+1
                # else:
                #     score=st.pop() + 2 * score
            #st.append(s[i])
        return score                     

            



