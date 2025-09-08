class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(x):
            return "0" not in str(x)
        
        for i in range(1,n):
            j=n-1
            if check(i) and check(j):
                return [i,j]
            
