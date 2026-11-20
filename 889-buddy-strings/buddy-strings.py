class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        freq1=Counter(s)
        freq2=Counter(goal)
        if len(s)!=len(goal):
            return False
        lst=[]   
        if freq1!=freq2:
            return False
        if s==goal:
            return any(i >1 for i in freq1.values())     
        for i in range(len(s)):
            if s[i]!=goal[i]:
                lst.append(i)
                if len(lst)>2:
                    return False
                # if (s.count(s[i])  + goal.count(goal[i]) )==2:
                #     return False
        return len(lst)==2