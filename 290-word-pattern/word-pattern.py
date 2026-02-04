class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        char={}
        word={}
        for ch ,w in zip(pattern,words):
            if ch in char :
                if char[ch]!=w:
                    return False 
            else:
                char[ch]=w
            if w in word:
                if word[w]!=ch:
                    return False
            else:
                 word[w]=ch 
        return True 
