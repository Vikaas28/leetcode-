class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq=Counter(answers)
        count=0
        for key, val in freq.items():
            group_size=key+1
            group_num=math.ceil(val/group_size)
            #print(num)
            count+=group_num*group_size
            #print(count)
        return count    