class Solution:
    def isHappy(self, n: int) -> bool:
        def square(x):
            return sum(int(i)**2 for i in str(x))
        o=n
        if n==1:
            return True
        while n>5:
            n=square(n)
            if n==1:
                return True
            if n==o:
                return False
        return False
