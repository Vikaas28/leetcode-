class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort()
        n=[str(num) for num in nums]
        def compare(x,y):
            return x+y>y+x
        def quickSort(arr):
            if len(arr)<=1:
                return arr
            pivot=arr[len(arr)//2]
            left=[x for x in arr if compare(x,pivot)]
            middle=[x for x in arr if x+pivot==pivot +x]
            right =[x for x in arr if compare(pivot ,x)]
            return quickSort(left)+middle +quickSort(right)
        arr=quickSort(n)   
        res="".join(arr)
        #return res   
        if res[0]=="0":
            return "0"
        else:
            return res          