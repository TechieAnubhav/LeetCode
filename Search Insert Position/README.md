# Search Insert Position

## Problem
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.  

You must write an algorithm with **O(log n)** runtime complexity.

---

**Example 1:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

---

**Constraints:**
- 1 <= nums.length <= 10⁴
- -10⁴ <= nums[i] <= 10⁴
- nums contains distinct values sorted in ascending order.
- -10⁴ <= target <= 10⁴

---

## Code
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i in sorted(nums):
            if target < i:
                a = nums.index(i)
                break
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        return a
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Check if `target` exists in `nums`. If so, return its index.  
2. If not found, iterate through the sorted array to find the first element greater than `target`.  
3. Store that index as the insertion position.  
4. If `target` is greater than the last element, return `len(nums)` (insert at end).  
5. If `target` is less than the first element, return `0` (insert at start).  
6. Return the stored index.

---

🛠️ **Possible Improvements**  
- This approach is **O(n)** because of the linear scan. Since the problem demands **O(log n)**, a binary search method should be used.  
- Python's `bisect_left` from the `bisect` module is an efficient built-in alternative.

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(n) — Uses linear search.  
- **Space Complexity:** O(1) — No extra storage used.
