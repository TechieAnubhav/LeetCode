class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        w=""
        for i in s.lower():
            if i.isalnum():
                r=i+r
                w=w+i
        if w==r:
            return True
        else:
            return False
          
