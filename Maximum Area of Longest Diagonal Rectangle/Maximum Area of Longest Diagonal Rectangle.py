class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        a=0
        d=0
        for i in dimensions:
            t=((i[0]**2)+(i[1]**2))**(1/2)
            if d==t:
                if a<i[0]*i[1]:
                    a=i[0]*i[1]
                    d=t
            elif d<t:
                d=t
                a=i[0]*i[1]
        return a
