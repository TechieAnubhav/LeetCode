# Longest Common Prefix

## Problem
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

## Examples

**Example 1:**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

---

## Constraints
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

---

## Code
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c=""
        strs=sorted(strs)
        f=strs[0]
        l=strs[-1]
        for i in range(min(len(f),len(l))):
            if f[i]!=l[i]:
                return c
            c+=f[i]
        return c
```

---

## 🧩 How I Solved It — Step-by-Step
1. Sort the array of strings.  
2. After sorting, only the first (`f`) and last (`l`) strings need to be compared since they will be the most different.  
3. Loop through the characters of `f` and `l` until a mismatch is found.  
4. Collect the common characters in `c`.  
5. Return `c` as the longest common prefix.  

---

## 🛠️ Possible Improvements
- Instead of sorting (`O(n log n)`), we could compare characters across all strings directly, which might save time for very large input.  
- Early stopping when one string becomes empty.  

---

## 🧠 Time & Space Complexity
- **Time Complexity:** `O(n log n + m)`  
  - Sorting takes `O(n log n)` where `n` is the number of strings.  
  - Comparing first and last strings takes `O(m)` where `m` is the length of the shortest string.  
- **Space Complexity:** `O(1)` — only uses extra variables.  
