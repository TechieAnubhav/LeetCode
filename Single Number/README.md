# Single Number

## Problem
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.  

You must implement a solution with **linear runtime complexity** and use only **constant extra space**.  

---

**Example 1:**
```
Input: nums = [2,2,1]
Output: 1
```

**Example 2:**
```
Input: nums = [4,1,2,1,2]
Output: 4
```

**Example 3:**
```
Input: nums = [1]
Output: 1
```

---

**Constraints:**
- 1 <= nums.length <= 3 * 10⁴  
- -3 * 10⁴ <= nums[i] <= 3 * 10⁴  
- Each element in the array appears twice except for one element which appears only once.  

---

## Code
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Use XOR to cancel out pairs of identical numbers.  
2. Since `a ^ a = 0` and `a ^ 0 = a`, all numbers that appear twice vanish.  
3. The one that appears once remains as the final result.  

---

🛠️ **Possible Improvements**  
- If multiple numbers appeared once instead of one, this approach wouldn’t work directly. We’d need hash maps or bitwise counting.  
- But for this specific problem, XOR is the most optimal.  

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(n) — each number is visited once.  
- **Space Complexity:** O(1) — no extra storage needed.  
