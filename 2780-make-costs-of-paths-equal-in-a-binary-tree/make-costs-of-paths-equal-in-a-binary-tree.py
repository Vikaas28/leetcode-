class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n-1, 1, -2):
               ans += abs(cost[i-1]-cost[i])
               cost[(i//2)-1] += max(cost[i-1], cost[i])
        return ans
        