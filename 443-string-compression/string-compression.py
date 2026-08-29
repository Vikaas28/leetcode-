class Solution:
    def compress(self, chars: List[str]) -> int:
        #s="".join(chars)


        i=0
        index=0

        n=len(chars)
    
        while i < n:
            curr=chars[i]
            count=0
            while i< n and chars[i]==curr:
                count+=1
                i+=1
            chars[index]=curr
            index+=1
            if count > 1:

                for ch in str(count):
                    chars[index]=ch
                    index+=1
        return index             

            
            

