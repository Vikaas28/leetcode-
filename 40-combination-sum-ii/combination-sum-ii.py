class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        arr=candidates
        arr.sort()
        def back(i,p,t):
            if t==0:
                res.append(p.copy())
                return
           
            for j in range(i,len(arr)):
                if j>i and arr[j] == arr[j-1]:
                    continue
                if arr[j]> t:
                    break 
                p.append(arr[j])
                back(j+1,p,t-arr[j])
                p.pop()
        back(0,[],target)
        return res             