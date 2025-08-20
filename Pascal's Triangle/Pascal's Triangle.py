class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(numRows):
            s=str(11**i)
            m=[]
            for j in s:
                m.append(int(j))
            l.append(m)
        return l
