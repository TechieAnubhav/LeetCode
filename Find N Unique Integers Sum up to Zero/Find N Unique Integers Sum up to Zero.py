class Solution:
    def sumZero(self, n: int) -> List[int]:
        l=[]
        if n%2==1:
            l=[i for i in range((n//2)*(-1),n//2+1)]
        else:
            l=[i for i in range(-n+1,n+1,2)]
        return l
