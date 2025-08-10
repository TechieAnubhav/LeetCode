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

## Code
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

---

🧩 **How I Solved It — Step-by-Step**  
1. Convert `n` to a string and sort its digits.  
2. Precompute all powers of 2 up to `2³⁰` (since 2³⁰ = 1,073,741,824 > 10⁹).  
3. For each power of 2, sort its digits and store them in a list.  
4. Check if the sorted string of `n` exists in the list of sorted power-of-two strings.  
5. Return `True` if found, else `False`.

---

🛠️ **Possible Improvements**  
- Use a `set` instead of a `list` for faster membership lookup.  
- Avoid recomputing the sorted powers of 2 every function call by storing them as a static precomputed variable.

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(1) — Only 30 fixed powers of 2 to check, each sort is on ≤ 10 digits.  
- **Space Complexity:** O(1) — Stores at most 30 sorted strings.
