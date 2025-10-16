class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        l=[0]*value
        for i in nums:
            j=i%value
            l[j]+=1
        r=0
        while l[r%value]>0:
            l[r%value]-=1
            r+=1
        return r
