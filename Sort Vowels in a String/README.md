# Sort Vowels in a String

## Problem
Given a string `s`, rearrange it to form a new string `t` such that:

1. All consonants remain in their original places.
2. The vowels ('a', 'e', 'i', 'o', 'u', in both lowercase and uppercase) are sorted in non-decreasing ASCII order.

Return the resulting string `t`.

---

## Examples

**Example 1:**
```
Input: s = "lEetcOde"
Output: "lEOtcede"
```
Explanation: The vowels 'E', 'O', 'e' are sorted to 'E', 'O', 'e' according to ASCII values. The consonants remain in their original positions.

**Example 2:**
```
Input: s = "lYmpH"
Output: "lYmpH"
```
Explanation: There are no vowels, so the string remains unchanged.

---

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of English alphabet letters in both lowercase and uppercase.

---

## Code
```python
class Solution:
    def sortVowels(self, s: str) -> str:
        v = []
        t = []
        
        # Collect all vowels in the string
        for i in s:
            if i in "aeiouAEIOU":
                v.append(i)
        
        # If there are no vowels, return the original string
        if not v:
            return s
        
        # Sort vowels by ASCII value
        v.sort()
        
        j = 0
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                t.append(v[j])
                j += 1
            else:
                t.append(s[i])
                
        return "".join(t)
```

---

## 🧩 How I Solved It — Step-by-Step
1. Iterated through the input string `s` and collected all vowels into a list `v`.
2. Sorted the list `v` by ASCII values.
3. Iterated through the string again:
   - If the character is a vowel, replaced it with the next vowel from the sorted list.
   - Otherwise, kept the original consonant.
4. Returned the result as a joined string.

---

## 🛠️ Possible Improvements
- Use a set for vowel lookup to optimize membership testing.
- Avoid creating two lists and work with the string indices more efficiently.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n log n), where `n` is the length of the string. Sorting the vowels list takes O(k log k) where `k` is the number of vowels, but in the worst case `k = n`.
- **Space Complexity:** O(n), as we store the vowels and result in separate lists.
