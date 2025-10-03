# Intersection of Two Arrays II

## Problem  
Given two integer arrays `nums1` and `nums2`, return an array of their intersection.  
Each element in the result must appear as many times as it shows in both arrays, and you may return the result in any order.  

---

**Example 1:**  
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

**Example 2:**  
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
```

---

**Constraints:**  
- 1 <= nums1.length, nums2.length <= 1000  
- 0 <= nums1[i], nums2[i] <= 1000  

---

## Code (Your Approach)
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                l.append(i)
        return l
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Iterate over each element in `nums1`.  
2. If the element exists in `nums2`, remove it from `nums2` (so duplicates are handled correctly).  
3. Append the element to the result list `l`.  
4. Return the final list `l`.  

---

🛠️ **Possible Improvements**  
- Current solution has **O(n × m)** worst-case complexity due to repeated `in` checks and `remove` operations.  
- Can be improved using:  
  - **HashMap / Counter approach** (count frequency of elements in both arrays, then take the minimum counts).  
  - Sorting both arrays and using two pointers for **O(n log n + m log m)** time.  

---

🧠 **Time & Space Complexity**  
- **Current approach:**  
  - Time: O(n × m) (checking membership + removing elements repeatedly).  
  - Space: O(min(n, m)) (result list).  
- **Optimized approach (Counter):**  
  - Time: O(n + m).  
  - Space: O(n + m).  
