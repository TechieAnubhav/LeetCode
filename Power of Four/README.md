# Power of Four

## Problem
Given an integer `n`, return `true` if it is a power of four. Otherwise, return `false`.  

An integer `n` is a power of four if there exists an integer `x` such that:  
```
n == 4^x
```

---

**Example 1:**
```
Input: n = 16
Output: true
```

**Example 2:**
```
Input: n = 5
Output: false
```

**Example 3:**
```
Input: n = 1
Output: true
```

---

**Constraints:**
- -2³¹ <= n <= 2³¹ - 1

---

## Code
```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        return n > 0 and 4 ** (round(math.log(n, 4))) == n
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Check if `n` is positive (powers of four are positive integers).  
2. Use logarithms to calculate `log₄(n)` via `math.log(n, 4)`.  
3. Round the result to the nearest integer to avoid floating-point errors.  
4. Raise 4 to that rounded integer power and compare it with `n`.  
5. Return `True` if they match, otherwise `False`.

---

🛠️ **Possible Improvements**  
- Avoid floating-point operations by repeatedly dividing `n` by 4 until it’s no longer divisible.  
- Use bitwise operations: check if `n` is a power of two and `n % 3 == 1` (property of powers of four).

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(1) — Logarithm calculation is constant time.  
- **Space Complexity:** O(1) — No extra memory used.
