# Roman to Integer

## Problem  
Roman numerals are represented by seven different symbols:  

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Rules:  
- Numerals are usually written largest to smallest, left to right.  
- Special subtraction cases:  
  - `I` before `V (5)` and `X (10)` → 4, 9  
  - `X` before `L (50)` and `C (100)` → 40, 90  
  - `C` before `D (500)` and `M (1000)` → 400, 900  

Given a Roman numeral string `s`, convert it to an integer.

---

## Examples  

**Example 1:**
```
Input: s = "III"
Output: 3
Explanation: III = 3
```

**Example 2:**
```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3
```

**Example 3:**
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4
```

---

## Constraints
- `1 <= s.length <= 15`  
- `s` contains only the characters: `'I', 'V', 'X', 'L', 'C', 'D', 'M'`  
- Guaranteed valid Roman numeral in range `[1, 3999]`

---

## Code
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                result += roman_to_int[s[i]]
        return result
```

---

## 🧩 How I Solved It — Step-by-Step
1. Created a mapping of Roman characters to integer values.  
2. Iterated through the string `s`.  
3. If the current value is **smaller than the next value**, subtract it (handles subtraction rules).  
4. Otherwise, add it to the result.  
5. Return the final accumulated integer.  

---

## 🛠️ Possible Improvements
- Instead of checking with `i + 1 < len(s)`, we could use a single-pass `zip` approach comparing `current` with `next`.  
- Could optimize further by pre-handling special cases like `IV`, `IX`, `XL`, etc., but current method is already clean and efficient.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** `O(n)` where `n` is the length of `s`.  
- **Space Complexity:** `O(1)` since the hashmap is fixed and independent of input size.  
