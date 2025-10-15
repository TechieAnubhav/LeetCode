# Adjacent Increasing Subarrays Detection II

## Problem
Given an array `nums` of n integers, your task is to find the maximum value of `k` for which there exist two adjacent subarrays of length `k` each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length `k` starting at indices `a` and `b` (`a < b`), where:

- Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are strictly increasing.
- The subarrays must be adjacent, meaning `b = a + k`.

Return the maximum possible value of `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

---

## Examples

### Example 1
**Input:**  
`nums = [2,5,7,8,9,2,3,4,3,1]`  
**Output:**  
`3`

**Explanation:**  
- The subarray starting at index 2 is `[7, 8, 9]`, which is strictly increasing.  
- The subarray starting at index 5 is `[2, 3, 4]`, which is also strictly increasing.  
These two subarrays are adjacent, and `3` is the maximum possible value of `k` for which two such adjacent strictly increasing subarrays exist.

---

### Example 2
**Input:**  
`nums = [1,2,3,4,4,4,4,5,6,7]`  
**Output:**  
`2`

**Explanation:**  
- The subarray `[1, 2]` is strictly increasing.  
- The subarray `[3, 4]` is also strictly increasing.  
They are adjacent, giving `k = 2`.

---

## Constraints
- `2 <= nums.length <= 2 * 10^5`  
- `-10^9 <= nums[i] <= 10^9`

---

## Code

```python
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res = 0
        up = 1
        prevUP = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up += 1
            else:
                prevUP = up
                up = 1
            if up > 2 * prevUP:
                prevUP = up // 2
            res = max(res, min(prevUP, up))
        return res
```

---

## 🧩 How I Solved It — Step-by-Step
1. Initialize counters for consecutive increasing elements (`up`) and previous increasing length (`prevUP`).
2. Iterate through the list:
   - If the current element is greater than the previous, increment `up`.
   - Otherwise, reset the streak and store the previous streak length in `prevUP`.
3. Adjust `prevUP` if the new streak is more than twice as long.
4. The potential `k` is the minimum of the two consecutive streaks (`min(prevUP, up)`).
5. Track the maximum such `k`.

---

## 🛠️ Possible Improvements
- Use a single pass with O(1) space (already optimal).
- Optional optimization: skip recalculating when the sequence length is already smaller than `2 * res`.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n) — one linear pass through the array.  
- **Space Complexity:** O(1) — only uses constant extra space.
