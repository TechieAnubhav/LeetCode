# Pow(x, n)

## Problem
Implement `pow(x, n)`, which calculates x raised to the power n (i.e., xⁿ).

## Examples

### Example 1
Input: x = 2.00000, n = 10  
Output: 1024.00000  

### Example 2
Input: x = 2.10000, n = 3  
Output: 9.26100  

### Example 3
Input: x = 2.00000, n = -2  
Output: 0.25000  
Explanation: 2⁻² = 1 / (2²) = 1/4 = 0.25  

## Constraints
- -100.0 < x < 100.0  
- -2³¹ <= n <= 2³¹ - 1  
- n is an integer.  
- Either x is not zero or n > 0.  
- -10⁴ <= xⁿ <= 10⁴  

## Code
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n
```

## 🧩 How I Solved It — Step-by-Step
1. Used Python’s built-in exponentiation operator `**` to compute powers.  
2. It directly handles positive, negative, and zero powers.  
3. For negative `n`, it computes reciprocal values automatically (e.g., `x ** -2 = 1 / (x ** 2)`).  

## 🛠️ Possible Improvements
- Implement **fast exponentiation (binary exponentiation)** for efficiency, especially when `n` is very large.  
- Avoid relying on `**` if an interview setting expects you to write it from scratch.  

## 🧠 Time & Space Complexity
- **Time Complexity:** O(1) (using built-in operator).  
- **Space Complexity:** O(1).  
