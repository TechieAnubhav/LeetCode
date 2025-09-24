# Valid Anagram

## Problem
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## Examples

### Example 1
Input:  
`s = "anagram", t = "nagaram"`  
Output:  
`true`

### Example 2
Input:  
`s = "rat", t = "car"`  
Output:  
`false`

## Constraints
- 1 <= s.length, t.length <= 5 * 10⁴  
- `s` and `t` consist of lowercase English letters  

## Code
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        for i in t:
            if i in s:
                s.remove(i)
            else:
                return False
        return True
```

## 🧩 How I Solved It — Step-by-Step
1. Checked if `s` and `t` have equal lengths. If not, return `False` immediately.  
2. Converted `s` into a list so characters can be removed when matched.  
3. Iterated through characters of `t`.  
   - If the character exists in `s`, removed it.  
   - If not, returned `False`.  
4. If all characters matched, returned `True`.  

## 🛠️ Possible Improvements
- The current solution has **O(n²)** time complexity due to list removal.  
- A better solution is to use sorting:  
  ```python
  return sorted(s) == sorted(t)
  ```  
  This runs in O(n log n).  

- The most efficient approach is to use **hashmaps / counters**:  
  ```python
  from collections import Counter
  return Counter(s) == Counter(t)
  ```  
  This runs in O(n).  

## 🧠 Time & Space Complexity
- **Current Solution:**  
  - Time Complexity: O(n²) (list removal is O(n) per operation).  
  - Space Complexity: O(n) (list copy of `s`).  

- **Sorting Solution:**  
  - Time Complexity: O(n log n).  
  - Space Complexity: O(n).  

- **Counter Solution (Best):**  
  - Time Complexity: O(n).  
  - Space Complexity: O(1) (since alphabet size is fixed at 26).  
