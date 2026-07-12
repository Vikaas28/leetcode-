class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        arr1=sorted(set(arr))
        ranks=defaultdict(int)
        res=[]
        for i in arr1:
            ranks[i]=len(ranks)+1
            print(ranks[i])
        for i in arr:    
            res.append(ranks[i])
        return res    