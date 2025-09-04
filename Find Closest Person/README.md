# Find Closest Person

## Problem
You are given three integers `x`, `y`, and `z`, representing the positions of three people on a number line:  

- `x` is the position of Person 1.  
- `y` is the position of Person 2.  
- `z` is the position of Person 3, who does not move.  

Both Person 1 and Person 2 move toward Person 3 at the same speed.  

Determine which person reaches Person 3 first:  
- Return `1` if Person 1 arrives first.  
- Return `2` if Person 2 arrives first.  
- Return `0` if both arrive at the same time.  

---

## Examples

**Example 1:**
```
Input: x = 2, y = 7, z = 4
Output: 1
Explanation: Person 1 reaches in 2 steps, Person 2 in 3 steps → Person 1 is closer.
```

**Example 2:**
```
Input: x = 2, y = 5, z = 6
Output: 2
Explanation: Person 1 takes 4 steps, Person 2 takes 1 step → Person 2 is closer.
```

**Example 3:**
```
Input: x = 1, y = 5, z = 3
Output: 0
Explanation: Both Person 1 and Person 2 take 2 steps → They reach together.
```

---

## Constraints
- `1 <= x, y, z <= 100`

---

## Code
```python
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(z - x)
        b = abs(z - y)
        if b < a:
            return 2
        elif a < b:
            return 1
        else:
            return 0
```

---

## 🧩 How I Solved It — Step-by-Step
1. Compute Person 1’s distance from Person 3 → `abs(z - x)`.  
2. Compute Person 2’s distance from Person 3 → `abs(z - y)`.  
3. Compare the distances:  
   - If Person 1’s distance is smaller → return `1`.  
   - If Person 2’s distance is smaller → return `2`.  
   - If equal → return `0`.  

---

## 🛠️ Possible Improvements
- Remove debugging `print()` statements for cleaner code.  
- Could be written in a single line using a conditional expression for brevity.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(1), only arithmetic operations and comparisons.  
- **Space Complexity:** O(1), constant extra space.  
