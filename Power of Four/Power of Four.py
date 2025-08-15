class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        return n>0 and 4**(round(math.log(n,4)))==n
