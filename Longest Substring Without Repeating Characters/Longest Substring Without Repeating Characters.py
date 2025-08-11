class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t=""
        p=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if (s[j] in t) and i!=j:
                    break
                t=t+s[j]
            if len(t)>len(p):
                    p=t
            t=""
        return len(p)
