class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def back(i,p, t):
            if t==target:
                res.append(p.copy())
                return 
            if t>target:
                return     
            for j in range(i,len(candidates)):
                p.append(candidates[j])
                back(j,p,t+candidates[j])
                p.pop()
        back(0,[],0)
        return res        