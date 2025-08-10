# Reordered Power of 2

## Problem
You are given an integer `n`. We reorder the digits in any order (including the original order) such that the leading digit is not zero.  

Return `true` if and only if we can do this so that the resulting number is a power of two.

---

**Example 1:**
```
Input: n = 1
Output: true
```

**Example 2:**
```
Input: n = 10
Output: false
```

---

**Constraints:**
- 1 <= n <= 10⁹

---

## Solution
We sort the digits of `n` and compare them with the sorted digits of all possible powers of 2 up to the constraint limit.  
If a match exists, then `n` can be reordered to form a power of two.

---

**Python Code:**
```python
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        s = "".join(sorted(s))
        p = []
        for i in range(30):
            a = str(2**i)
            a = "".join(sorted(a))
            p.append(a)
        return s in p
```
