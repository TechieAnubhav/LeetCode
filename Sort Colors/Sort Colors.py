class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq=[0]*3
        for i in nums:
            freq[i]+=1
        c=0
        for i in range(3):
            nums[c:c+freq[i]]=[i]*freq[i]
            c+=freq[i]
