class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=0
        curr=0
        for i in range(len(nums)):
            if nums[i] ==1:
                curr+=1
            else:
                maxx=max(maxx,curr)
                curr=0
        maxx=max(maxx,curr)
        return maxx
