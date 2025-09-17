# Length of Last Word

## Problem
Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

---

## Examples

**Example 1:**
```
Input: s = "Hello World"
Output: 5
```
**Explanation:**  
The last word is "World" with length 5.

**Example 2:**
```
Input: s = "   fly me   to   the moon  "
Output: 4
```
**Explanation:**  
The last word is "moon" with length 4.

**Example 3:**
```
Input: s = "luffy is still joyboy"
Output: 6
```
**Explanation:**  
The last word is "joyboy" with length 6.

---

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

---

## Code
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split()[-1])
```

---

## 🧩 How I Solved It — Step-by-Step
1. Used `rstrip()` to remove trailing spaces from the string.
2. Split the string into a list of words using `split()`.
3. Selected the last word using `[-1]`.
4. Returned the length of the last word using `len()`.

---

## 🛠️ Possible Improvements
- This solution is already efficient and concise.
- Alternatively, you could traverse the string from the end to avoid using extra space from splitting.

---

## 🧠 Time & Space Complexity

- **Time Complexity:** O(n), where n is the length of the string `s`, due to splitting and scanning.
- **Space Complexity:** O(n), for storing the list of words after splitting.
