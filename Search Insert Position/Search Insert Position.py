class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i in sorted(nums):
            if target<i:
                a=nums.index(i)
                break
        if target>nums[-1]:
            return len(nums)
        if target<nums[0]:
            return 0
        return a
