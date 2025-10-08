# Valid Palindrome II

## Problem
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

---

**Example 1:**
```
Input: s = "aba"
Output: true
```

**Example 2:**
```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

**Example 3:**
```
Input: s = "abc"
Output: false
```

---

**Constraints:**
- 1 <= s.length <= 10⁵  
- s consists of lowercase English letters.  

---

## Code
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(st,left,right):
            while left<right:
                if st[left]!=st[right]:
                    return False
                left+=1
                right-=1
            return True
        
        left,right=0,len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return check(s,left+1,right) or check(s,left,right-1)
        return True
```

---

🧩 **How I Solved It — Step-by-Step**
1. Use two pointers (`left`, `right`) to check if the string is a palindrome.  
2. When characters differ, try skipping either the left or right character and check again.  
3. If either case forms a palindrome, return `True`. Otherwise, return `False`.

---

🛠️ **Possible Improvements**
- Could optimize slightly by early stopping once mismatch count exceeds 1.  
- For very large strings, recursion can be avoided for efficiency (iterative check).

---

🧠 **Time & Space Complexity**
- **Time:** O(n) — Single pass check plus up to one extra check.  
- **Space:** O(1) — Constant extra memory used.
