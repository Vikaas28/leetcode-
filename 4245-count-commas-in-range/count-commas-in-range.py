class Solution:
    def countCommas(self, n: int) -> int:
        return sum(f"{i:,}".count(',') for i in range(1, n + 1))