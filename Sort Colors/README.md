# Sort Colors

## Problem
Given an array `nums` with n objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers **0**, **1**, and **2** to represent the color red, white, and blue, respectively.

You must solve this problem **without using the library's sort function**.

---

## Examples

### Example 1
**Input:** nums = [2,0,2,1,1,0]  
**Output:** [0,0,1,1,2,2]

### Example 2
**Input:** nums = [2,0,1]  
**Output:** [0,1,2]

---

## Constraints
- n == nums.length  
- 1 <= n <= 300  
- nums[i] is either 0, 1, or 2

---

## Code
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq=[0]*3
        for i in nums:
            freq[i]+=1
        c=0
        for i in range(3):
            nums[c:c+freq[i]]=[i]*freq[i]
            c+=freq[i]
```

---

## 🧩 How I Solved It — Step-by-Step
1. Created a frequency array `freq` of size 3 to count occurrences of each color (0, 1, 2).  
2. Iterated through `nums` and incremented the count for each number.  
3. Reconstructed `nums` in-place using the counts from `freq` so that all 0s, then 1s, then 2s appear consecutively.

---

## 🛠️ Possible Improvements
- Could implement the **Dutch National Flag algorithm** (single-pass, constant space).  
- The current approach uses two passes (one for counting, one for writing).

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n) — Two linear passes over the array.  
- **Space Complexity:** O(1) — Only a fixed-size frequency array is used.
