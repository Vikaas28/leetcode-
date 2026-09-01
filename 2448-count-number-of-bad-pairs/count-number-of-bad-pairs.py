class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # count =0
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if i < j and j -i != nums[j]- nums[i]:
        #             count+=1
        # return count 

        freq=defaultdict(int)
        good=0

        n=len(nums)
        total=n*(n-1)//2
        i=0

        for num in nums:
            key=num-i
            good+=freq[key]
            freq[key]+=1
            i+=1

        return total-good

        