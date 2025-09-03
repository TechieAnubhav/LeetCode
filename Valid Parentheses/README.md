# Valid Parentheses

## Problem
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.  

An input string is valid if:  
1. Open brackets must be closed by the same type of brackets.  
2. Open brackets must be closed in the correct order.  
3. Every close bracket has a corresponding open bracket of the same type.  

---

## Examples

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Example 4:**
```
Input: s = "([])"
Output: true
```

**Example 5:**
```
Input: s = "([)]"
Output: false
```

---

## Constraints
- `1 <= s.length <= 10^4`  
- `s` consists of parentheses only `'()[]{}'`.  

---

## Code
```python
class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        a = []
        for i in range(len(s)):
            if s[i] in "([{":
                a.append(s[i])
            else:
                if not a:
                    return False
                top = a.pop()
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False
        return len(a) == 0
```

---

## 🧩 How I Solved It — Step-by-Step
1. Initialize an empty stack `a`.  
2. Traverse each character in the string.  
3. If it’s an opening bracket (`(`, `[`, `{`), push it onto the stack.  
4. If it’s a closing bracket, check if the top of the stack matches the correct opening bracket.  
   - If not, return `False`.  
5. After processing all characters, if the stack is empty, return `True`; otherwise, return `False`.  

---

## 🛠️ Possible Improvements
- Could use a dictionary mapping `{')':'(', ']':'[', '}':'{'}` to simplify conditions.  
- Early exit for odd-length strings, since they can’t form valid pairs.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n), where `n` is the length of the string. Each character is processed once.  
- **Space Complexity:** O(n), for the stack in the worst case (all opening brackets).  
