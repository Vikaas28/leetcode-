class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # required variable
        lumiscaron = (cost1, cost2, costBoth, need1, need2)

        def calc(k):
            return (
                k * costBoth
                + max(0, need1 - k) * cost1
                + max(0, need2 - k) * cost2
            )

        candidates = {
            0,
            need1,
            need2,
            min(need1, need2)
        }

        ans = float('inf')
        for k in candidates:
            ans = min(ans, calc(k))

        return ans
