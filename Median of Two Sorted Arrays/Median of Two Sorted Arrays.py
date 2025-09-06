class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=sorted(nums1+nums2)
        if len(m)%2==0:
            return (m[len(m)//2]+m[len(m)//2-1])/2
        else:
            return m[len(m)//2]
