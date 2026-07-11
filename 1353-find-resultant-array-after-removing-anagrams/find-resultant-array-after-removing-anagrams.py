class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def anagram(s1,s2):
            letter1={}
            letter2={}
            for i in s1:
                letter1[i]=letter1.get(i,0)+1
            for i in s2:
                letter2[i]=letter2.get(i,0)+1    
            return letter1==letter2
        i=1
        while i<len(words):
        #for i in range(1,len(words)):
            if anagram(words[i],words[i-1]):
                words.pop(i)
            else:
                i+=1

        return words                