class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=list(map(str, digits))
        a=int("".join(a))
        a=a+1
        s=str(a)
        l=list(s)
        for i in range(len(l)):
            l[i]=int(l[i])
        return l
