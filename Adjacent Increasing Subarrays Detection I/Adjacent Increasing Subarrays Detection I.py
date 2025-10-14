class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k==1 and len(nums)>=2:
            return True
        inc=1
        prev=0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                inc+=1
            else:
                prev=inc
                inc=1
            if (prev>=k and inc>=k) or prev>=2*k or inc>=2*k:
                return True
        return False
