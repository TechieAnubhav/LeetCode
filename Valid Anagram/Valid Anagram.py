class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=list(s)
        for i in t:
            if i in s:
                a=s.remove(i)
            else:
                return False
        return True
