# Minimum Operations to Make the Integer Zero

## Problem
You are given two integers `num1` and `num2`.

In one operation, you can choose an integer `i` in the range `[0, 60]` and subtract `2^i + num2` from `num1`.

Return the **minimum number of operations** needed to make `num1` equal to `0`.

If it is impossible to make `num1` equal to `0`, return `-1`.

---

## Examples

**Example 1:**
```
Input: num1 = 3, num2 = -2
Output: 3
Explanation:
- Choose i = 2 → 3 - (2^2 + (-2)) = 3 - (4 - 2) = 1
- Choose i = 2 → 1 - (2^2 + (-2)) = 1 - (4 - 2) = -1
- Choose i = 0 → -1 - (2^0 + (-2)) = -1 - (1 - 2) = 0
Total operations = 3
```

**Example 2:**
```
Input: num1 = 5, num2 = 7
Output: -1
Explanation: It is impossible to make 5 equal to 0 with the given operations.
```

---

## Constraints
- `1 <= num1 <= 10^9`
- `-10^9 <= num2 <= 10^9`

---

## Code
```python
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # try up to 60 operations
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():  # check if x can be expressed with k powers of 2
                return k
        return -1
```

---

## 🧩 How I Solved It — Step-by-Step
1. Each operation subtracts `(2^i + num2)` from `num1`.  
2. After `k` operations, the effect is:  
   ```
   num1 - num2*k = sum of k powers of 2
   ```
3. This means `num1 - num2*k` must be decomposable into **exactly k powers of 2**.  
4. That is possible if:  
   - `num1 - num2*k >= k` (since we need at least `1` per power of 2), and  
   - `x.bit_count() <= k` (binary representation has at most `k` set bits).  
5. Try all `k` from 1 to 60 (because `2^60` covers up to `10^18`), return the smallest valid `k`.  

---

## 🛠️ Possible Improvements
- Add early pruning if `num1 < num2` in some cases.  
- Use math reasoning to skip invalid ranges instead of brute-forcing all `k`.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(60) = O(1), since we only check at most 60 values of `k`.  
- **Space Complexity:** O(1), only a few integer variables.  
