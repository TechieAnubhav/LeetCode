class Solution:
    def sortVowels(self, s: str) -> str:
        v=[]
        t=[]
        for i in s:
            if i in "aeiouAEIOU":
                v.append(i)
        if v==[]:
            return s
        
        v.sort()
        if len(v)==len(s):
            return "".join(v)
        j=0
        for i in range(len(s)):
            if s[i] not in v:
                t.append(s[i])
            else:
                t.append(v[j])
                j+=1
        return "".join(t)
