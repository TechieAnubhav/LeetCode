class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i not in d:
                d[i]=""
            else:
                return True
                break
        else:
            return False
