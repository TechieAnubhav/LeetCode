class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s=str(n)
        s="".join(sorted(s))
        p=[]
        for i in range(30):
            a=str(2**i)
            a="".join(sorted(a))
            p.append(a)

        return s in p
            
