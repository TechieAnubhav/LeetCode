# 🔢 LeetCode - Palindrome Number

## 📝 Problem Statement

Given an **integer** `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a **palindrome** when it reads the same backward as forward.

---

## 📌 Examples

**Example 1:**  
**Input**: `x = 121`  
**Output**: `true`  
**Explanation**: Reads as `121` from both directions.

**Example 2:**  
**Input**: `x = -121`  
**Output**: `false`  
**Explanation**: From left to right: `-121`. From right to left: `121-` → Not a palindrome.

**Example 3:**  
**Input**: `x = 10`  
**Output**: `false`  
**Explanation**: Reversed: `01` → Not a palindrome.

---

## 📚 Constraints

- `-2^31 <= x <= 2^31 - 1`

---

## ✅ My Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

```markdown
## 🧩 How I Solved It — Step-by-Step

1. **Convert to String**  
   Convert the integer `x` to a string using `str(x)`.

2. **Reverse the String**  
   Use Python’s slicing feature `[::-1]` to reverse the string.

3. **Compare Strings**  
   Check if the original string and the reversed string are equal.

4. **Return the Result**  
   - If they are equal → return `True` (it is a palindrome).  
   - Else → return `False` (not a palindrome).

---

## 🧠 Time & Space Complexity

- **Time Complexity**: `O(n)`  
  Where `n` is the number of digits in `x`. String reversal and comparison both take linear time.

- **Space Complexity**: `O(n)`  
  Because a reversed copy of the string is created in memory.

---

## 🛠️ Possible Improvements

To reduce space complexity:

- Avoid converting the integer to a string.  
- Use mathematical operations to reverse only half the number and compare.  
- This brings space complexity down to `O(1)`.

---

## 🔗 Tags

`math`, `palindrome`, `leetcode-easy`, `integer`
