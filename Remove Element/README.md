# Remove Element

## Problem
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.  

Consider the number of elements in `nums` which are not equal to `val` be `k`. To get accepted, you need to:  
- Change the array `nums` so that the first `k` elements contain the elements not equal to `val`.  
- The remaining elements of `nums` do not matter.  
- Return `k`.

---

**Example 1:**
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: The function returns k = 2, with the first two elements being 2.
```

**Example 2:**
```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: The function returns k = 5, with the first five elements containing 0, 0, 1, 3, and 4 (order may vary).
```

---

**Constraints:**
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

---

## Code
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in nums:
            if i != val:
                nums[index] = i
                index += 1
        return index
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Initialize a pointer `index` at 0 to track the position for storing valid elements.  
2. Iterate through each element `i` in `nums`.  
3. If `i` is not equal to `val`, place it at `nums[index]` and increment `index`.  
4. At the end, `index` will represent the count `k` of elements not equal to `val`.  
5. Return `index`.

---

🛠️ **Possible Improvements**  
- Use two pointers (`left` and `right`) to minimize assignments when many values equal `val` are present at the start.  
- Early stop if all remaining elements are equal to `val`.

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(n) — Single pass through the array.  
- **Space Complexity:** O(1) — In-place modification without extra storage.
