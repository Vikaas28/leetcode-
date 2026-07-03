class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        res=[]
        for key , val in freq.items():
            if val==1 and key - val not in freq and key + val not in freq:
                res.append(key)
        return res         