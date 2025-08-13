class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        return n>0 and 3**(round(math.log(n,3)))==n
