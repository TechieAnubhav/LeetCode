# 🧠 LeetCode - Valid Palindrome

## 📝 Problem Statement

A **phrase is a palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

**Alphanumeric characters** include **letters** and **numbers**.

### 🔹 Given:  
A string `s`

### 🔹 Return:  
`true` if it is a palindrome, otherwise `false`.

---

## 📌 Examples

**Example 1:**  
**Input**: `s = "A man, a plan, a canal: Panama"`  
**Output**: `true`  
**Explanation**: After removing non-alphanumerics and converting to lowercase: `"amanaplanacanalpanama"`, which is a palindrome.

**Example 2:**  
**Input**: `s = "race a car"`  
**Output**: `false`  
**Explanation**: `"raceacar"` is not a palindrome.

**Example 3:**  
**Input**: `s = " "`  
**Output**: `true`  
**Explanation**: Empty string after cleaning is considered a palindrome.

---

## 📚 Constraints

- `1 <= s.length <= 2 * 10^5`  
- `s` consists only of **printable ASCII** characters.

---

## ✅ My Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        w=""
        for i in s.lower():
            if i.isalnum():
                r=i+r
                w=w+i
        if w==r:
            return True
        else:
            return False
```

---

## 🧩 How I Solved It — Step-by-Step

1. **Convert to Lowercase**:  
   - I converted the entire string to lowercase using `s.lower()` to make it case-insensitive.

2. **Filter Alphanumeric Characters**:  
   - I iterated through each character in the string.  
   - If it was alphanumeric (`i.isalnum()`), I kept it.

3. **Create Two Versions of the Cleaned String**:  
   - `w`: Stored the cleaned string in normal order.  
   - `r`: Stored the cleaned string in reverse order.

4. **Compare Both Strings**:  
   - If `w` is equal to `r`, it's a palindrome → return `True`.  
   - Otherwise, return `False`.

---

## 🧠 Time & Space Complexity

- **Time Complexity**: `O(n)` — Linear traversal of the input string.
- **Space Complexity**: `O(n)` — Due to the two auxiliary strings `w` and `r`.

---

## 🛠️ Possible Improvements

Instead of storing two separate strings, we can optimize space using a **two-pointer approach**:
- Start from both ends of the string.
- Skip non-alphanumeric characters.
- Compare characters while moving inward.
- This would reduce space complexity to `O(1)`.

---

## 🔗 Tags

`string`, `two-pointers`, `palindrome`, `leetcode-easy`