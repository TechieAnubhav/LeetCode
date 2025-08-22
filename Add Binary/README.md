# Add Binary

## Problem
Given two binary strings `a` and `b`, return their sum as a binary string.

---

**Example 1:**
```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**
```
Input: a = "1010", b = "1011"
Output: "10101"
```

---

**Constraints:**
- 1 <= a.length, b.length <= 10⁴  
- `a` and `b` consist only of '0' or '1'.  
- Each string does not contain leading zeros except for the zero itself.  

---

## Code (Pythonic Approach)
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Convert binary strings to integers with `int(x, 2)`.  
2. Add the integers.  
3. Convert the sum back to binary with `bin(x)[2:]`.  

---

🛠️ **Possible Improvements**  
- If asked in an interview, implement a **manual bit-by-bit addition with carry** to avoid relying on built-in big integers.  
- Manual solution also works in languages without automatic big integer support.  

---

🧠 **Time & Space Complexity**  
- **Pythonic approach:**  
  - Time: O(n) (conversion + addition + conversion back).  
  - Space: O(n) (for storing converted values).  
- **Manual approach:**  
  - Time: O(n) (traverses strings once).  
  - Space: O(n) (for result string).  
