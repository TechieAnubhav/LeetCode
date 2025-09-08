# Convert Integer to the Sum of Two No-Zero Integers

## Problem
A **No-Zero integer** is a positive integer that does not contain any `0` in its decimal representation.

Given an integer `n`, return a list of two integers `[a, b]` where:
- `a` and `b` are No-Zero integers.
- `a + b = n`.

The test cases guarantee at least one valid solution. If multiple solutions exist, return any.

---

## Examples

**Example 1:**
```
Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1. Both are No-Zero integers, and 1 + 1 = 2.
```

**Example 2:**
```
Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9. Both are No-Zero integers, and 2 + 9 = 11.
Other valid answers such as [8,3] are also acceptable.
```

---

## Constraints
- `2 <= n <= 10^4`

---

## Code
```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(x):
            return "0" not in str(x)
        
        for i in range(1, n):
            j = n - i
            if check(i) and check(j):
                return [i, j]
```

---

## 🧩 How I Solved It — Step-by-Step
1. Define a helper `check(x)` that returns `True` if `x` contains no zero.  
2. Iterate from `1` to `n-1`.  
3. For each `i`, compute `j = n - i`.  
4. If both `i` and `j` are No-Zero integers, return `[i, j]`.  
5. The loop always finds a valid solution due to problem constraints.

---

## 🛠️ Possible Improvements
- This brute-force approach is fine for `n <= 10^4`.  
- For larger inputs, you could generate candidates directly by avoiding numbers containing zero.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n * d), where `d` is the number of digits (checking zeros in each number). For `n <= 10^4`, this is efficient.  
- **Space Complexity:** O(1), as only constant extra space is used.  
