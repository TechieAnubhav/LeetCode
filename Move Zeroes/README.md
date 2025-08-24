# Move Zeroes

## Problem
Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements.  
You must do this **in-place** without making a copy of the array.

---

**Example 1:**
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Example 2:**
```
Input: nums = [0]
Output: [0]
```

---

**Constraints:**
- 1 <= nums.length <= 10⁴  
- -2³¹ <= nums[i] <= 2³¹ - 1  

---

## Code
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Use two pointers:  
   - `l` = index for placing the next non-zero.  
   - `r` = current index while scanning.  
2. Traverse array with `r`.  
3. If `nums[r]` is non-zero, swap it with `nums[l]` and increment `l`.  
4. By the end, all non-zeros are at the start, and zeros are pushed to the end.  

---

🛠️ **Possible Improvements**  
- Current solution is already **optimal**.  
- Another option: count non-zeros, overwrite them, then fill rest with zeros (still O(n), but less intuitive).  

---

🧠 **Time & Space Complexity**  
- Time: **O(n)** (single pass).  
- Space: **O(1)** (in-place).  
