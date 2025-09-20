# Intersection of Two Arrays

## Problem
Given two integer arrays nums1 and nums2, return an array of their intersection.  
Each element in the result must be unique and you may return the result in any order.

## Examples

### Example 1
Input: nums1 = [1,2,2,1], nums2 = [2,2]  
Output: [2]  

### Example 2
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]  
Output: [9,4]  
Explanation: [4,9] is also accepted.  

## Constraints
- 1 <= nums1.length, nums2.length <= 1000  
- 0 <= nums1[i], nums2[i] <= 1000  

## Code
```python
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

## 🧩 How I Solved It — Step-by-Step
1. Convert both arrays into sets to remove duplicates.  
2. Use the `&` operator to get common elements between the two sets.  
3. Convert the intersection back into a list.  
4. Return the list as the final result.  

## 🛠️ Possible Improvements
- Sort the result before returning if consistent ordering is required.  
- For very large arrays, use hashing manually instead of built-in set operations for memory efficiency.  

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n + m), where n = len(nums1), m = len(nums2).  
- **Space Complexity:** O(n + m), for storing both sets.  
