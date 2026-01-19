class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(open_cnt, close_cnt, path):
            # base case
            if open_cnt == close_cnt == n:
                res.append(path)
                return

            # add "("
            if open_cnt < n:
                backtrack(open_cnt + 1, close_cnt, path + "(")

            # add ")"
            if close_cnt < open_cnt:
                backtrack(open_cnt, close_cnt + 1, path + ")")

        backtrack(0, 0, "")
        return res
