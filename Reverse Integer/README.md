# Reverse Integer

## Problem
Given a signed 32-bit integer `x`, return `x` with its digits reversed.  
If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.  
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

---

## Examples

**Example 1:**
```
Input: x = 123
Output: 321
```

**Example 2:**
```
Input: x = -123
Output: -321
```

**Example 3:**
```
Input: x = 120
Output: 21
```

---

## Constraints
- `-2^31 <= x <= 2^31 - 1`

---

## Code
```python
class Solution:
    def reverse(self, x: int) -> int:
        t = x
        if x >= 0:
            a = int(str(x)[::-1])
        else:
            x = x * -1
            a = int(str(x)[::-1])
        if a <= 2**31:
            if t >= 0:
                return a
            else:
                return a * -1
        else:
            return 0
```

---

## 🧩 How I Solved It — Step-by-Step
1. Store the original value of `x` in `t`.  
2. If `x` is non-negative, reverse its digits by converting to string and using slicing.  
3. If `x` is negative, make it positive, reverse its digits, and reapply the negative sign later.  
4. Check if the reversed integer is within the 32-bit signed integer limit (`2^31`).  
5. If within the limit, return the reversed integer with the correct sign.  
6. Otherwise, return `0`.

---

## 🛠️ Possible Improvements
- Avoid converting to string by reversing the digits mathematically using modulo and division operations.  
- Handle overflow by checking boundaries during the reversing process instead of after.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(d), where `d` is the number of digits in `x`.  
- **Space Complexity:** O(d), due to converting the integer to a string for manipulation.
