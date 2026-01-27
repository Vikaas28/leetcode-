class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v=['a','e','i','o','u']
        for c in s:
            if c in v:
                return True 
        return False        