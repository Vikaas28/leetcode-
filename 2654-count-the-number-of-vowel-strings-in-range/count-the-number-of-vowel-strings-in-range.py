class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        count =0
        vowels="aeiou"
        char=set(list((vowels)))
        print(char)
    
        for i in range(left, right+1):
            w=words[i]
            if w[0] in char and  w[-1] in char:
                count +=1
        return count            

            
        