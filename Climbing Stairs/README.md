# Climbing Stairs

## Problem
You are climbing a staircase. It takes `n` steps to reach the top.  

Each time you can either climb **1 step** or **2 steps**.  
Return the number of distinct ways you can climb to the top.

---

## Examples

**Example 1:**
```
Input: n = 2
Output: 2
```
**Explanation:**  
There are two ways to climb to the top:  
1. 1 step + 1 step  
2. 2 steps  

**Example 2:**
```
Input: n = 3
Output: 3
```
**Explanation:**  
There are three ways to climb to the top:  
1. 1 step + 1 step + 1 step  
2. 1 step + 2 steps  
3. 2 steps + 1 step  

---

## Constraints
- `1 <= n <= 45`

---

## Code
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b
```

---

## 🧩 How I Solved It — Step-by-Step
1. Recognized this as a **Fibonacci sequence problem**:
   - Ways(n) = Ways(n-1) + Ways(n-2).
2. Handled base cases:
   - 1 way to climb 0 or 1 step.
   - 2 ways to climb 2 steps.
3. Used an iterative loop to build up the result instead of recursion to improve efficiency.
4. Returned the final value for `n`.

---

## 🛠️ Possible Improvements
- Use **memoization** or **recursion with caching** (less efficient than iterative for this problem, but cleaner to implement).
- Space can be optimized to only track the last two states (already done in this solution).

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n) — single loop up to `n`.
- **Space Complexity:** O(1) — only two variables are maintained.
