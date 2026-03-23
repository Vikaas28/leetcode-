from collections import defaultdict

class Solution:
    def distance(self, nums):
        n = len(nums)
        res = [0] * n
        
        mp = defaultdict(list)
        
        # Step 1: group indices
        for i, num in enumerate(nums):
            mp[num].append(i)
        
        # Step 2: process each group
        for indices in mp.values():
            prefix = [0]
            
            # build prefix sum of indices
            for idx in indices:
                prefix.append(prefix[-1] + idx)
            
            m = len(indices)
            
            for k in range(m):
                i = indices[k]
                
                # left
                left = i * k - prefix[k]
                
                # right
                right = (prefix[m] - prefix[k+1]) - i * (m - k - 1)
                
                res[i] = left + right
        
        return res