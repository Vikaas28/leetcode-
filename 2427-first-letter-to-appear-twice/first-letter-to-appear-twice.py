class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter=[]
        for i in s :
            if i in letter:
                return i 
            else:
                letter.append(i)
