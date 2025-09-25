# Max Consecutive Ones

## Problem
Given a binary array `nums`, return the maximum number of consecutive 1's in the array.

## Examples
**Example 1:**
```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

**Example 2:**
```
Input: nums = [1,0,1,1,0,1]
Output: 2
```

## Constraints
- 1 <= nums.length <= 10^5  
- nums[i] is either 0 or 1.

## Code
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            else:
                maxx = max(maxx, curr)
                curr = 0
        maxx = max(maxx, curr)
        return maxx
```

## 🧩 How I Solved It — Step-by-Step
1. Maintain two counters:  
   - `maxx` for the longest streak of 1s.  
   - `curr` for the current streak of 1s.  
2. Traverse through the array:  
   - If the element is `1`, increment `curr`.  
   - If the element is `0`, update `maxx` and reset `curr`.  
3. After finishing the loop, compare again to catch the case where the array ends with 1s.  
4. Return the maximum streak found.

## 🛠️ Possible Improvements
- The loop can be simplified by iterating directly over numbers instead of indices:
```python
for num in nums:
    if num == 1:
        curr += 1
    else:
        maxx = max(maxx, curr)
        curr = 0
```

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n) — single pass through the array.  
- **Space Complexity:** O(1) — constant memory used.
