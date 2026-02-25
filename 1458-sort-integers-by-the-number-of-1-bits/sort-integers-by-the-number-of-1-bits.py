class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def CountBits(num):
            count=0
            while num:
                if num&1:
                    count+=1
                num>>=1
            return count
        temp={}
        for num in arr:
            val=CountBits(num) 
            if val in temp:
                temp[val].append(num)
            else:
                temp[val]=[num]
        result=[]
        for key in sorted(temp.keys()):
            result.extend(sorted(temp[key]))
        return result
        