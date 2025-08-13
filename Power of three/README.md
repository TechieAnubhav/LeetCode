# Power of Three

## Problem
Given an integer `n`, return `true` if it is a power of three. Otherwise, return `false`.  

An integer `n` is a power of three if there exists an integer `x` such that:  
```
n == 3^x
```

---

**Example 1:**
```
Input: n = 27
Output: true
Explanation: 27 = 3^3
```

**Example 2:**
```
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.
```

**Example 3:**
```
Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).
```

---

**Constraints:**
- -2³¹ <= n <= 2³¹ - 1

---

## Code
```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        return n > 0 and 3 ** (round(math.log(n, 3))) == n
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Check if `n` is positive (since negative numbers and zero cannot be powers of three).  
2. Use logarithms to compute `log₃(n)` by `math.log(n, 3)`.  
3. Round the result to the nearest integer to handle floating-point precision issues.  
4. Raise 3 to that rounded power and check if it equals `n`.  
5. Return `True` if equal, else `False`.

---

🛠️ **Possible Improvements**  
- Avoid floating-point errors completely by iteratively dividing `n` by 3 until it is no longer divisible.  
- Precompute the maximum power of three within the integer range and check divisibility directly.

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(1) — Logarithm calculation is constant time.  
- **Space Complexity:** O(1) — No extra space used.
