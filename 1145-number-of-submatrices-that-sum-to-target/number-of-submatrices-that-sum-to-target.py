class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):

                matrix[i][j]+=matrix[i][j-1]
        #print(matrix)    
        count=0
        for c1 in range(len(matrix[0])):
            for c2 in range(c1,len(matrix[0])):
                mp={0:1}
                
                prefix=0
                k=target 
                summ=0

                for r in range(len(matrix)):
                    summ=matrix[r][c2] -(matrix[r][c1-1] if c1 >0 else 0)
                    prefix+=summ
                    if prefix - k in mp :
                        count+=mp.get(prefix-k,0)
                    mp[prefix]=mp.get(prefix,0)+1
        return count                    
                