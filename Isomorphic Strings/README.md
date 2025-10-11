# Isomorphic Strings

## Problem
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

---

**Example 1:**
```
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
```

**Example 2:**
```
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.
```

**Example 3:**
```
Input: s = "paper", t = "title"
Output: true
```

---

**Constraints:**
- 1 <= s.length <= 5 * 10⁴  
- t.length == s.length  
- s and t consist of any valid ASCII character.  

---

## Code
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(t))==len(set(zip(s,t)))
```

---

🧩 **How I Solved It — Step-by-Step**
1. Created pairs of corresponding characters from `s` and `t` using `zip`.
2. Used sets to check if mappings are consistent and unique both ways.
3. Verified that:
   - Number of unique characters in `s` equals number of unique characters in `t`.
   - Number of unique (s[i], t[i]) pairs also equals them — ensuring one-to-one mapping.

---

🛠️ **Possible Improvements**
- Could explicitly create two dictionaries to track forward and reverse mappings for clarity.
- That version is slightly slower but more intuitive for interviews.

---

🧠 **Time & Space Complexity**
- **Time:** O(n) — one pass through both strings.  
- **Space:** O(n) — to store unique pairs and characters.
