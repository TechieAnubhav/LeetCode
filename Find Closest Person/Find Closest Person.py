class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a=abs(z-x)
        b=abs(z-y)
        print(a,b)
        if b<a:
            return 2
        elif a<b:
            return 1
        else:
            return 0
