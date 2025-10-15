class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res=0
        up=1
        prevUP=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                up+=1
            else:
                prevUP=up
                up=1
            if up>2*prevUP:
                prevUP=up//2
            res=max(res,min(prevUP,up))
        return res
