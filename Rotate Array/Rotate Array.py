# Rotate Array

## Problem
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Example 1
**Input:** `nums = [1,2,3,4,5,6,7]`, `k = 3`  
**Output:** `[5,6,7,1,2,3,4]`  
**Explanation:**  
- rotate 1 step to the right: `[7,1,2,3,4,5,6]`  
- rotate 2 steps to the right: `[6,7,1,2,3,4,5]`  
- rotate 3 steps to the right: `[5,6,7,1,2,3,4]`  

### Example 2
**Input:** `nums = [-1,-100,3,99]`, `k = 2`  
**Output:** `[3,99,-1,-100]`  
**Explanation:**  
- rotate 1 step to the right: `[99,-1,-100,3]`  
- rotate 2 steps to the right: `[3,99,-1,-100]`  

### Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            l = nums.pop()
            nums.insert(0, l)
```

## 🧩 How I Solved It — Step-by-Step
1. The `pop()` function removes the last element of the list.
2. The `insert(0, l)` function adds the popped element to the beginning.
3. Repeating this `k` times rotates the array `k` steps to the right.

## 🛠️ Possible Improvements
- The current approach has **O(n * k)** time complexity, which is inefficient for large `k`.
- A more optimal solution uses array slicing:  
  `nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]` (O(n) time).

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n * k)
- **Space Complexity:** O(1)
