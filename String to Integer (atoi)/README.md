# String to Integer (atoi)

## Problem
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer. The conversion follows these rules:

1. **Whitespace**: Ignore any leading whitespace characters `' '`.
2. **Signedness**: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positive if neither is present.
3. **Conversion**: Read digits until a non-digit character is encountered or the end of the string is reached. Skip leading zeros. If no digits are read, return `0`.
4. **Rounding**: Clamp the result within the 32-bit signed integer range `[-2^31, 2^31 - 1]`.

Return the integer as the final result.

---

## Examples

**Example 1:**
```
Input: s = "42"
Output: 42
```

**Example 2:**
```
Input: s = "   -42"
Output: -42
```

**Example 3:**
```
Input: s = "4193 with words"
Output: 4193
```

**Example 4:**
```
Input: s = "words and 987"
Output: 0
```

**Example 5:**
```
Input: s = "-91283472332"
Output: -2147483648
```

---

## Constraints
- `0 <= s.length <= 200`
- `s` consists of printable ASCII characters.

---

## Code
```python
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if we've reached the end
        if i == n:
            return 0
        
        # Step 2: Check for sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # Step 3: Read digits and convert
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            
            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX
            
            i += 1
        
        # Step 4: Apply sign and return
        return res * sign
```

---

## 🧩 How I Solved It — Step-by-Step
1. Defined constants `INT_MAX` and `INT_MIN` for clamping.
2. Skipped all leading spaces using a loop.
3. Detected if the next character is a sign (`+` or `-`) and set the `sign` variable accordingly.
4. Iterated through each digit character, building the result while checking for overflow or underflow at each step.
5. Applied the sign and returned the clamped result.

---

## 🛠️ Possible Improvements
- Handle overflow more efficiently by checking before updating `res`.
- Use regular expressions to parse the number, although it may not be as explicit or performant.
- Validate input in real-world scenarios for robustness.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n), where `n` is the length of the input string.
- **Space Complexity:** O(1), only constant space is used for counters and result variables.
