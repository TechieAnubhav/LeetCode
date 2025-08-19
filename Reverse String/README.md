# Reverse String

## Problem
Write a function that reverses a string. The input string is given as an array of characters `s`.  
You must do this by modifying the input array **in-place** with **O(1) extra memory**.

---

**Example 1:**
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:**
```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

---

**Constraints:**
- 1 <= s.length <= 10^5  
- s[i] is a printable ASCII character.  

---

## Code
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Strings are given as character arrays.  
2. To reverse in-place, we swap the first and last characters, then move inward.  
3. Loop only halfway (n//2) so we don’t swap back.  
4. Swapping is done using tuple unpacking in Python.  
5. No extra memory is used — only swaps inside the array.  

---

🛠️ **Possible Improvements**  
- In Python, a one-liner using slicing is possible:  
  ```python
  s[:] = s[::-1]
  ```  
  But in interviews, the two-pointer approach is preferred since it shows you understand in-place operations.  

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(n) — each character is touched at most once.  
- **Space Complexity:** O(1) — only constant extra space is used for swapping.  
