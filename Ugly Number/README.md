# Ugly Number

## Problem
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

---

**Example 1:**
```
Input: n = 6
Output: true
Explanation: 6 = 2 × 3
```

**Example 2:**
```
Input: n = 1
Output: true
Explanation: 1 has no prime factors.
```

**Example 3:**
```
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
```

---

**Constraints:**
- -2³¹ <= n <= 2³¹ - 1

---

## Code
```python
class Solution:
    def isUgly(self, n: int) -> bool:
        while n>=1:
            if n==1:
                return True
            elif n%2==0:
                n=n//2
            elif n%3==0:
                n=n//3
            elif n%5==0:
                n=n//5
            else:
                return False
        return False
```

---

🧩 **How I Solved It — Step-by-Step**
1. Check if n is less than 1 → immediately return False since ugly numbers are positive.
2. Divide n repeatedly by 2, 3, or 5 whenever possible.
3. If at any point n becomes 1 → it’s an ugly number.
4. If n is not divisible by 2, 3, or 5 and not 1 → return False.

---

🛠️ **Possible Improvements**
- Add an early check for `n <= 0` for clarity.
- Use a loop with `[2,3,5]` to make code shorter.

---

🧠 **Time & Space Complexity**
- **Time Complexity:** O(log n) — each division reduces n by a factor.
- **Space Complexity:** O(1) — constant space used.
