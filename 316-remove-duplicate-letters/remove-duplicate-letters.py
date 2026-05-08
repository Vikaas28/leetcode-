class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char=list(s)
        freq=Counter(s)
        stack=[]
        dis=set()
        for c in s:
            freq[c]-=1
            if c in dis:
                continue
            while stack and c < stack[-1] and freq[stack[-1]]>0:
                top=stack.pop()
                dis.remove(top)
            stack.append(c)
            dis.add(c)
        return ''.join(stack)                   