class Solution:
    def maxFreqSum(self, s: str) -> int:
        v={}
        c={}
        for i in s:
            if i in "aeiou":
                if i in v:
                    v[i]+=1
                else:
                    v[i]=1
            else:
                if i in c:
                    c[i]+=1
                else:
                    c[i]=1
        if v=={}:
            v={0:0}
        if c=={}:
            c={0:0}
        return max(v.values())+max(c.values())
