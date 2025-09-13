# Find Most Frequent Vowel and Consonant

## Problem
You are given a string `s` consisting of lowercase English letters ('a' to 'z').

Your task is to:

1. Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
2. Find the consonant (all other letters excluding vowels) with the maximum frequency.
3. Return the sum of the two frequencies.

**Note:**  
- If multiple vowels or consonants have the same maximum frequency, you may choose any one of them.  
- If there are no vowels or no consonants in the string, consider their frequency as 0.  
- The frequency of a letter is the number of times it occurs in the string.

---

## Examples

**Example 1:**
```
Input: s = "successes"
Output: 6
```
**Explanation:**  
Vowels: 'u' (1), 'e' (2), max frequency = 2  
Consonants: 's' (4), 'c' (2), max frequency = 4  
Total = 2 + 4 = 6

**Example 2:**
```
Input: s = "aeiaeia"
Output: 3
```
**Explanation:**  
Vowels: 'a' (3), 'e' (2), 'i' (2), max frequency = 3  
No consonants present, so frequency = 0  
Total = 3 + 0 = 3

---

## Constraints

- `1 <= s.length <= 100`
- `s` consists of lowercase English letters only.

---

## Code
```python
class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = {}
        c = {}
        
        for char in s:
            if char in "aeiou":
                v[char] = v.get(char, 0) + 1
            else:
                c[char] = c.get(char, 0) + 1
        
        max_vowel = max(v.values()) if v else 0
        max_consonant = max(c.values()) if c else 0
        
        return max_vowel + max_consonant
```

---

## 🧩 How I Solved It — Step-by-Step
1. Initialized two dictionaries: one for vowels (`v`) and one for consonants (`c`).
2. Iterated through the string and updated the frequency counts accordingly.
3. Checked if the dictionaries are empty, and assigned 0 if there are no vowels or consonants.
4. Used `max()` to find the maximum frequency in each dictionary.
5. Returned the sum of the maximum vowel and consonant frequencies.

---

## 🛠️ Possible Improvements
- Optimize by using `collections.Counter`.
- Avoid checking for empty dictionaries by initializing with default values.

---

## 🧠 Time & Space Complexity
- **Time Complexity:** O(n), where n is the length of the string, since we traverse the string once and find the max in each dictionary.
- **Space Complexity:** O(1), because the alphabet size is fixed (at most 26 characters for both vowels and consonants).
