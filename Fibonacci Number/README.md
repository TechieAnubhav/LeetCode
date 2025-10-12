# Fibonacci Number

## Problem
The Fibonacci numbers, commonly denoted F(n), form a sequence such that each number is the sum of the two preceding ones, starting from 0 and 1.  
That is:

F(0) = 0, F(1) = 1  
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

---

## Examples

**Example 1:**
```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

**Example 2:**
```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

**Example 3:**
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

---

## Constraints
- 0 <= n <= 30

---

## Code
```python
class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            return f(n-1)+f(n-2)
        return f(n)
```

---

🧩 **How I Solved It — Step-by-Step**
1. Define a helper function `f(n)` that recursively computes the Fibonacci number.
2. Base cases: return 0 for n=0 and 1 for n=1.
3. For all other cases, return the sum of the previous two Fibonacci numbers.
4. Return the result of `f(n)`.

---

🛠️ **Possible Improvements**
- Use **memoization** (either manually or via `functools.lru_cache`) to avoid repeated calculations and improve efficiency.
- Alternatively, use **iterative** or **dynamic programming** approach for O(n) time and O(1) space.

---

🧠 **Time & Space Complexity**
- **Recursive approach:**  
  - Time: O(2ⁿ) (due to repeated subproblems)  
  - Space: O(n) (recursive stack depth)
- **Optimized DP approach:**  
  - Time: O(n)  
  - Space: O(1)
