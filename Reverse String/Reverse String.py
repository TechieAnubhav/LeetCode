class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)%2==0:
            for i in range(len(s)//2):
                s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
        if len(s)%2!=0:
            for i in range(len(s)//2):
                s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
        
        
