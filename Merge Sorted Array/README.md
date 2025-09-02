# Merge Sorted Array

## Problem
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.  

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.  

The final sorted array should not be returned by the function, but instead stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

---

## Examples

**Example 1:**
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

**Example 2:**
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

**Example 3:**
```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
```

---

## Constraints
- `nums1.length == m + n`  
- `nums2.length == n`  
- `0 <= m, n <= 200`  
- `1 <= m + n <= 200`  
- `-10^9 <= nums1[i], nums2[j] <= 10^9`  

---

## Code
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        len1 = len(nums1)
        end_idx = len1 - 1
        while n > 0 and m > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_idx] = nums2[n-1]
                n -= 1
            else:
                nums1[end_idx] = nums1[m-1]
                m -= 1
            end_idx -= 1
        while n > 0:
            nums1[end_idx] = nums2[n-1]
            n -= 1
            end_idx -= 1
```

---

## 🧩 How I Solved It — Step-by-Step
1. Start from the end of both arrays (`nums1[m-1]` and `nums2[n-1]`).  
2. Compare the elements, place the larger one at the end of `nums1`.  
3. Decrease pointers (`m` or `n`) accordingly.  
4. If elements remain in `nums2`, copy them over to the start of `nums1`.  
5. This ensures an in-place merge without using extra space.  

---

## 🛠️ Possible Improvements
- Could implement a two-pointer approach starting from the beginning, but it would need extra space.  
- Current reverse approach is optimal since it avoids shifting elements.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(m + n), since each element
