class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        a=[]
        for i in range(len(s)):
            if s[i] in "([{":
                a.append(s[i])
            else:
                if not a:
                    return False
                top=a.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return len(a)==0
