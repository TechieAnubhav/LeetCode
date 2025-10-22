# Ransom Note

## Problem
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

### Example 1:
**Input:** ransomNote = "a", magazine = "b"  
**Output:** false

### Example 2:
**Input:** ransomNote = "aa", magazine = "ab"  
**Output:** false

### Example 3:
**Input:** ransomNote = "aa", magazine = "aab"  
**Output:** true

### Constraints:
- 1 <= ransomNote.length, magazine.length <= 10^5  
- ransomNote and magazine consist of lowercase English letters.

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in list(set(ransomNote)):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
```

---

### 🧩 How I Solved It — Step-by-Step
1. Converted `ransomNote` into a set to avoid duplicate checks.
2. For each unique character, compared its count in `ransomNote` and `magazine`.
3. If `ransomNote` needs more of any character than available in `magazine`, returned `False`.
4. Otherwise, returned `True`.

### 🛠️ Possible Improvements
- Use `collections.Counter` for O(n) efficiency instead of repeated `count()` calls.
- Example optimized version:
  ```python
  from collections import Counter
  class Solution:
      def canConstruct(self, ransomNote: str, magazine: str) -> bool:
          return not (Counter(ransomNote) - Counter(magazine))
  ```

### 🧠 Time & Space Complexity
- **Time Complexity:** O(n * m) in current version due to multiple count() calls.  
- **Space Complexity:** O(1) (ignoring input storage).
