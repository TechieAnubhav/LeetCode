# Longest Substring Without Repeating Characters

## Problem
Given a string `s`, find the length of the longest substring without duplicate characters.

---

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

---

**Constraints:**
- 0 <= s.length <= 5 * 10⁴
- s consists of English letters, digits, symbols and spaces.

---

## Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = ""
        p = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if (s[j] in t) and i != j:
                    break
                t = t + s[j]
            if len(t) > len(p):
                p = t
            t = ""
        return len(p)
```

---

🧩 **How I Solved It — Step-by-Step**  
1. Initialize two empty strings `t` (for building substrings) and `p` (to store the longest found substring).  
2. Use a nested loop: the outer loop picks the starting index, and the inner loop extends the substring until a duplicate character is found.  
3. If a duplicate is encountered, break the inner loop.  
4. Compare the length of `t` with `p`; if longer, update `p`.  
5. Reset `t` for the next starting position.  
6. Return the length of `p`.

---

🛠️ **Possible Improvements**  
- Use a sliding window with a `set` or `dict` to track characters and achieve O(n) time complexity.  
- Avoid string concatenation in loops (costly in Python) and use indexes for substring length tracking.

---

🧠 **Time & Space Complexity**  
- **Time Complexity:** O(n²) — Due to nested loops and character search.  
- **Space Complexity:** O(n) — For storing temporary substrings.
