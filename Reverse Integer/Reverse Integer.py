class Solution:
    def reverse(self, x: int) -> int:
        t=x
        if x>=0:
            a=int(str(x)[::-1])
        else:
            x=x*-1
            a=int(str(x)[::-1])
        if a<=2**31:
            if t>=0:
                return a
            else:
                return a*-1
        else:
             return 0
