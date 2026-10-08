class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        deep=0
        for ch in s :
            if ch =="(":
                if deep >0:
                    res.append(ch)
                deep+=1
            else:
                deep-=1
                if deep >0:
                    res.append(ch)
        return "".join(res)                    