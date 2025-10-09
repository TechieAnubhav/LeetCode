class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ma=max(nums)
        mi=min(nums)
        gcd=1
        for i in range(2,mi+1):
            if ma%i==0 and mi%i==0:
                gcd=i
        return gcd
