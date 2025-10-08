class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(st,left,right):
            while left<right:
                if st[left]!=st[right]:
                    return False
                left+=1
                right-=1
            return True
        
        left,right=0,len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return check(s,left+1,right) or check(s,left,right-1)
        return True
