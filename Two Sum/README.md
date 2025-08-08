# 🧮 Two Sum

## 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return **indices** of the **two numbers** such that they **add up to target**.

You may **assume exactly one solution** exists, and you **may not use the same element twice**.

Return the answer in **any order**.

---

## 📌 Examples

### Example 1

**Input:**  
`nums = [2,7,11,15]`, `target = 9`  
**Output:** `[0,1]`  
**Explanation:** `nums[0] + nums[1] == 9`

---

### Example 2

**Input:**  
`nums = [3,2,4]`, `target = 6`  
**Output:** `[1,2]`

---

### Example 3

**Input:**  
`nums = [3,3]`, `target = 6`  
**Output:** `[0,1]`

---

## 📚 Constraints

- `2 <= nums.length <= 10^4`  
- `-10^9 <= nums[i], target <= 10^9`  
- Only **one valid answer** exists.

---

## ✅ My Solution (Python)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i, j]

```
### ✅ Block 2 — Explanation, Complexity, and Improvements


## 🧩 How I Solved It — Step-by-Step

1. **Loop through all indices `i` in `nums`.**  
2. **For each `i`, loop again through all indices `j`.**  
3. **Skip if `i == j`.**  
4. **If `nums[i] + nums[j] == target`, return `[i, j]`.**  
5. **End early since only one valid pair exists.**

---

## 🧠 Time & Space Complexity

- **Time Complexity:** `O(n^2)`  
  Because of the nested loop comparing every pair.

- **Space Complexity:** `O(1)`  
  No extra data structures used.

---

## 🛠️ Possible Improvements

- Use a **hashmap (dictionary)** to reduce time to `O(n)`.  
  Track the index of each value as you iterate and check for `target - nums[i]` in the map.

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
