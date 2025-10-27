# Happy Number

## Problem
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

### Example 1
Input: n = 19  
Output: true  
Explanation:  
1² + 9² = 82  
8² + 2² = 68  
6² + 8² = 100  
1² + 0² + 0² = 1

### Example 2
Input: n = 2  
Output: false  

### Constraints
1 <= n <= 2³¹ - 1

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def square(x):
            return sum(int(i)**2 for i in str(x))
        o = n
        if n == 1:
            return True
        while n > 5:
            n = square(n)
            if n == 1:
                return True
            if n == o:
                return False
        return False
```

---

## 🧩 How I Solved It — Step-by-Step
1. I created a helper function `square()` that calculates the sum of squares of digits.  
2. Then I loop through the transformation process while `n > 5` because all unhappy numbers eventually fall below 5 (and none below 5 except 1 are happy).  
3. I checked if the number repeats (`n == o`) to detect cycles.  
4. If we reach 1, return `True`; otherwise, `False`.

---

## 🛠️ Possible Improvements
- Use a `set` to track seen numbers instead of comparing with `o` to catch cycles more robustly.  
- Add input validation for edge cases.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(log n) — because the number of digits reduces quickly as we square and sum.  
- **Space Complexity:** O(1) — constant extra space.
