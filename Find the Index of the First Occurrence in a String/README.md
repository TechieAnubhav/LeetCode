# Find the Index of the First Occurrence in a String

## Problem
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

---

## Examples

**Example 1:**
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
```
**Explanation:**  
"sad" occurs at index 0 and 6. The first occurrence is at index 0.

**Example 2:**
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
```
**Explanation:**  
"leeto" did not occur in "leetcode".

---

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

---

## Code
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
```

---

## 🧩 How I Solved It — Step-by-Step
1. Iterated through each character in `haystack`.
2. Checked if the current character matches the first character of `needle`.
3. If it matches, compared the slice of `haystack` from the current index to the length of `needle`.
4. If the substring matches `needle`, returned the index.
5. If no match is found after checking all possibilities, returned -1.

---

## 🛠️ Possible Improvements
- Limit the loop range to `len(haystack) - len(needle) + 1` to avoid unnecessary checks at the end.
- Handle the case where `needle` is an empty string explicitly if required by the problem.

---

## 🧠 Time & Space Complexity

- **Time Complexity:** O((n-m+1) * m), where n is the length of `haystack` and m is the length of `needle`.
- **Space Complexity:** O(m), used for slicing substrings during comparison.
