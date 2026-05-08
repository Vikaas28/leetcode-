class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq={}
        dis=set()
        freq=Counter(s)
        stack=[]
        for c in s:
            freq[c]-=1
            if c in dis:
                continue
            while stack and stack[-1] > c and freq[stack[-1]] >0:
                top=stack.pop()
                dis.remove(top)
            stack.append(c)
            dis.add(c)
        return ''.join(stack)           
