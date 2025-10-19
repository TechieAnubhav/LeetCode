class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                c+=1
        if nums[-1]>nums[0]:
            c+=1
        return c<=1                
