class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        s=a+b
        s=bin(s)[2:]
        return s
            
