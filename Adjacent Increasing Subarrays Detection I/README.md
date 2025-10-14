# Adjacent Increasing Subarrays Detection I

## Problem
Given an array `nums` of n integers and an integer `k`, determine whether there exist **two adjacent subarrays** of length `k` such that both subarrays are **strictly increasing**.  

Specifically, check if there are two subarrays starting at indices `a` and `b` (`a < b`), where:
- Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are strictly increasing.  
- The subarrays must be adjacent, meaning `b = a + k`.

Return `true` if it is possible to find two such subarrays, and `false` otherwise.

---

## Examples

**Example 1:**
```
Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3
Output: true
Explanation:
The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, so the result is true.
```

**Example 2:**
```
Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5
Output: false
```

---

## Constraints
- 2 <= nums.length <= 100  
- 1 < 2 * k <= nums.length  
- -1000 <= nums[i] <= 1000  

---

## Code
```python
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1 and len(nums) >= 2:
            return True
        inc = 1
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                prev = inc
                inc = 1
            if (prev >= k and inc >= k) or prev >= 2 * k or inc >= 2 * k:
                return True
        return False
```

---

🧩 **How I Solved It — Step-by-Step**
1. If `k == 1`, then any two elements side by side will satisfy the condition — return `True`.
2. Use two counters:
   - `inc`: length of the current increasing sequence.
   - `prev`: length of the previous increasing sequence before a break.
3. Iterate through the array:
   - If `nums[i] > nums[i-1]`, increment `inc`.
   - Otherwise, store the previous `inc` into `prev` and reset `inc` to 1.
4. Check if:
   - both `prev` and `inc` are at least `k`, or  
   - either sequence itself has length ≥ `2 * k` (it contains both subarrays).  
   - If yes, return `True`.
5. If no condition is met after traversal, return `False`.

---

🛠️ **Possible Improvements**
- Can optimize readability by precomputing lengths of increasing streaks and scanning once.  
- Could be extended to find **how many** such adjacent subarrays exist instead of just returning `True` or `False`.  

---

🧠 **Time & Space Complexity**
- **Time Complexity:** O(n) — single pass through the array.  
- **Space Complexity:** O(1) — only constant extra space used.
