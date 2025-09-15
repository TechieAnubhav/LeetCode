class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split()
        c=0
        for i in l:
            s=set(i)
            for j in brokenLetters:
                if j in s:
                    break
            else:
                c+=1
        return c
