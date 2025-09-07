# Find N Unique Integers Sum up to Zero

## Problem
Given an integer `n`, return any array containing `n` unique integers such that they add up to 0.

---

## Examples

**Example 1:**
```
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3], [-3,-1,2,-2,4].
```

**Example 2:**
```
Input: n = 3
Output: [-1,0,1]
```

**Example 3:**
```
Input: n = 1
Output: [0]
```

---

## Constraints
- `1 <= n <= 1000`

---

## Code
```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = []
        if n % 2 == 1:
            l = [i for i in range((n // 2) * (-1), n // 2 + 1)]
        else:
            l = [i for i in range(-n + 1, n + 1, 2)]
        return l
```

---

## 🧩 How I Solved It — Step-by-Step
1. If `n` is odd, include zero and symmetric pairs like `-k` and `k`.  
2. If `n` is even, exclude zero and use pairs like `-k` and `k`.  
3. Use list comprehensions to build the result easily.  
4. The generated list is guaranteed to sum to zero.

---

## 🛠️ Possible Improvements
- The solution is concise and efficient.  
- Alternatively, you could always build half the array and append their negatives, adding zero if needed.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n), as the list is built in linear time.  
- **Space Complexity:** O(n), to store the result array.
