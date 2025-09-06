# Median of Two Sorted Arrays

## Problem
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median** of the two sorted arrays.

The overall run time complexity should be **O(log (m+n))**.

---

## Examples

**Example 1:**
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:**
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2+3)/2 = 2.5.
```

---

## Constraints
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

---

## Code
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = sorted(nums1 + nums2)
        if len(m) % 2 == 0:
            return (m[len(m)//2] + m[len(m)//2 - 1]) / 2
        else:
            return m[len(m)//2]
```

---

## 🧩 How I Solved It — Step-by-Step
1. Merge both sorted arrays into one list.  
2. Sort the combined list.  
3. If the list length is **even**, take the average of the two middle elements.  
4. If the list length is **odd**, take the middle element directly.  

---

## 🛠️ Possible Improvements
- This solution runs in **O((m+n) log(m+n))** due to sorting.  
- For optimal **O(log(min(m,n)))**, use binary search to partition the arrays instead of merging and sorting.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O((m+n) log(m+n)) because of sorting.  
- **Space Complexity:** O(m+n) for storing the merged list.  
