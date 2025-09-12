class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for i in s:
            if i in "aeiouAEIOU":
                return True
        return False
