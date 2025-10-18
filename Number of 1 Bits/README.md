# Number of 1 Bits

## Problem
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

### Example 1:
Input: n = 11  
Output: 3  
Explanation: The input binary string 1011 has a total of three set bits.

### Example 2:
Input: n = 128  
Output: 1  
Explanation: The input binary string 10000000 has a total of one set bit.

### Example 3:
Input: n = 2147483645  
Output: 30  
Explanation: The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

### Constraints:
1 <= n <= 2³¹ - 1

## Code
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
```

---

## 🧩 How I Solved It — Step-by-Step
1. Initialize a counter to zero.
2. Use the bit manipulation trick `n = n & (n - 1)` which removes the lowest set bit in every iteration.
3. Continue until n becomes zero, counting how many times we can remove a set bit.
4. The final count gives the number of set bits in the binary representation of n.

---

## 🛠️ Possible Improvements
- We could precompute the bit counts for bytes (0–255) and use a lookup table for larger numbers to optimize performance.
- In Python, we can also use `bin(n).count('1')`, though it’s less efficient.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(k), where k is the number of set bits in n.
- **Space Complexity:** O(1)
