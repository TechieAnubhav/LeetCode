# Reordered Power of 2

## Problem Statement
You are given an integer `n`. You can reorder the digits in any order (including the original order) such that the leading digit is not zero.  

Return `true` if and only if we can do this so that the resulting number is a power of two.

---

### Example 1:
```
Input: n = 1
Output: true
```

### Example 2:
```
Input: n = 10
Output: false
```

---

### Constraints:
- 1 <= n <= 10⁹

---

## Approach
We can solve this by:
1. Sorting the digits of `n`.
2. Precomputing all powers of 2 up to the largest possible value within the constraint.
3. Sorting the digits of each power of 2.
4. Checking if the sorted digit string of `n` matches any precomputed sorted power of 2 string.

Since there are only 30 possible powers of 2 within this range, the check is efficient.

---

## Complexity
- **Time Complexity:** O(1) — Fixed range of powers of 2.
- **Space Complexity:** O(1) — Small constant space for storing digit patterns.
```pyhton
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
