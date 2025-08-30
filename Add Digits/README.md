# Add Digits

## Problem  
Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

---

## Examples  

**Example 1:**
```
Input: num = 38
Output: 2
Explanation: 
38 --> 3 + 8 = 11  
11 --> 1 + 1 = 2  
Since 2 has only one digit, return it.
```

**Example 2:**
```
Input: num = 0
Output: 0
```

---

## Constraints
- `0 <= num <= 2^31 - 1`

---

## Code
```python
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum = 0
            while num > 0:
                sum = sum + num % 10
                num = num // 10
            num = sum
        return num
```

---

## 🧩 How I Solved It — Step-by-Step
1. While `num` has **2 or more digits**, keep reducing it.  
2. Initialize a temporary `sum` to store the digit sum.  
3. Extract digits one by one using modulus (`num % 10`) and floor division (`num // 10`).  
4. After processing all digits, assign `sum` back to `num`.  
5. Repeat until `num` is a single digit.  

---

## 🛠️ Possible Improvements
- Use the **digital root formula** for constant-time solution:  
  ```
  if num == 0: return 0
  return 1 + (num - 1) % 9
  ```
- This avoids loops and works in O(1) time.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** `O(log n)` in the worst case (number of digits in `num`).  
- **Space Complexity:** `O(1)` — only a few variables are used.  
