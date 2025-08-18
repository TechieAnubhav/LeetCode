# Contains Duplicate

## Problem
Given an integer array `nums`, return **true** if any value appears at least twice in the array, and return **false** if every element is distinct.

---

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.
```

**Example 3:**
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

---

**Constraints:**
- 1 <= nums.length <= 10^5  
- -10^9 <= nums[i] <= 10^9  

---

## Code
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Create an empty set `seen` to store unique elements.  
2. Loop through each number in `nums`.  
3. If the number is already in `seen`, return `True`.  
4. Otherwise, add it to the set.  
5. If loop finishes without finding duplicates, return `False`.  

---

🛠️ **Possible Improvements**  
- You can solve this problem in one line with:  
  ```python
  return len(nums) != len(set(nums))
  ```  
- However, the loop version is clearer for interviews.  

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(n) — each lookup and insertion in a set is O(1) on average.  
- **Space Complexity:** O(n) — extra space for the set storing unique numbers.  
