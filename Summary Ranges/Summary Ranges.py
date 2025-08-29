class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l=[]
        m=[]
        for i in range(len(nums)):
            if len(l)>0 and nums[i]!=l[-1]+1:
                if len(l)==1:
                    m.append(f"{l[0]}")
                    l.clear()
                else:
                    m.append(f"{l[0]}->{l[-1]}")
                    l.clear()
            l.append(nums[i])
        if len(l)==1:
            m.append(f"{l[0]}")
        elif len(l)>1:
            m.append(f"{l[0]}->{l[-1]}")
        return m
