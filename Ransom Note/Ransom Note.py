class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in list(set(ransomNote)):
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True
